import pandas as pd
from google.cloud import bigquery
from google.auth import load_credentials_from_file

def extract_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    df = pd.read_csv(url)
    return df

def transform_data(df):
    return df.groupby("species", as_index=False).mean()

def load_to_bigquery(df, creds_path, project_id, dataset_id, table_id):
    creds, _ = load_credentials_from_file(creds_path)
    client = bigquery.Client(credentials=creds, project=project_id)

    table_ref = f"{project_id}.{dataset_id}.{table_id}"
    job = client.load_table_from_dataframe(df, table_ref)
    job.result()

    print(f"Tabla cargada correctamente: {table_ref}")

def validate(project_id, dataset_id, table_id, creds_path):
    creds, _ = load_credentials_from_file(creds_path)
    client = bigquery.Client(credentials=creds, project=project_id)

    table_ref = f"{project_id}.{dataset_id}.{table_id}"
    query = f"SELECT * FROM `{table_ref}`"

    df = client.query(query).to_dataframe()
    print(df.head())

if __name__ == "__main__":
    creds_path = "credentials/service_account.json"
    project_id = "eloquent-hangar-474417-t1"
    dataset_id = "demo_dataset"
    table_id = "iris_summary"

    df_raw = extract_data()
    df_transformed = transform_data(df_raw)

    load_to_bigquery(df_transformed, creds_path, project_id, dataset_id, table_id)
    validate(project_id, dataset_id, table_id, creds_path)
