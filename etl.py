import pandas as pd
from google.cloud import bigquery
from google.auth import load_credentials_from_file
from google.cloud.bigquery import LoadJobConfig, WriteDisposition

def extract_data() -> pd.DataFrame:
    """
    Extract step of the ETL pipeline.
    Loads the Iris dataset from a public GitHub repository.
    """
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    df = pd.read_csv(url)
    return df

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform step.
    Groups the dataset by species and computes mean values
    for all numerical columns.
    """
    df_transformed = df.groupby("species", as_index=False).mean()
    return df_transformed

def load_to_bigquery(df: pd.DataFrame, creds_path: str, project_id: str,
                     dataset_id: str, table_id: str) -> None:
    """
    Load step.
    Uploads the transformed DataFrame to Google BigQuery.
    Uses WRITE_TRUNCATE to avoid duplicates (replace full table).
    """
    creds, _ = load_credentials_from_file(creds_path)
    client = bigquery.Client(credentials=creds, project=project_id)

    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    job_config = LoadJobConfig(
        write_disposition=WriteDisposition.WRITE_TRUNCATE  # always overwrite table
    )

    job = client.load_table_from_dataframe(
        df, table_ref, job_config=job_config
    )
    job.result()

    print(f"Data successfully loaded into: {table_ref}")

def validate(creds_path: str, project_id: str, dataset_id: str, table_id: str) -> None:
    """
    Validation step.
    Performs a SELECT * query to confirm that data was loaded correctly.
    """
    creds, _ = load_credentials_from_file(creds_path)
    client = bigquery.Client(credentials=creds, project=project_id)

    table_ref = f"{project_id}.{dataset_id}.{table_id}"
    query = f"SELECT * FROM `{table_ref}`"

    df = client.query(query).to_dataframe()
    print("\nPreview of loaded data:")
    print(df)

if __name__ == "__main__":
    # Static configuration (sync with notebook)
    creds_path = "credentials/service_account.json"
    project_id = "eloquent-hangar-474417-t1"
    dataset_id = "demo_dataset"
    table_id = "iris_summary"

    print("Running ETL pipeline...\n")

    df_raw = extract_data()
    df_transformed = transform_data(df_raw)

    load_to_bigquery(df_transformed, creds_path, project_id, dataset_id, table_id)
    validate(creds_path, project_id, dataset_id, table_id)

    print("\nETL pipeline completed successfully.")
