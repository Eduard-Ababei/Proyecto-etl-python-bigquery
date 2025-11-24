# ETL Pipeline with Python and Google BigQuery

This project implements a complete ETL (Extract–Transform–Load) workflow using Python, pandas, and Google BigQuery.  
It demonstrates how to integrate a local data analysis environment with a cloud-based data warehouse, replicating a realistic Data Engineering scenario.

---

## 1. Overview

The pipeline executes the three core stages of an ETL process:

- **Extract:** load a public dataset from a remote repository.  
- **Transform:** clean, aggregate, and compute summary statistics using pandas.  
- **Load:** upload the transformed results into a BigQuery table through the official Google Cloud API.

This project serves as a practical reference for connecting Python with Google Cloud Platform, handling service account authentication, client initialization, dataset management, and SQL querying.

---

## 2. Technologies Used

| Category | Tool / Library |
|----------|----------------|
| Language | Python 3.x |
| Data Wrangling | pandas |
| Cloud Platform | Google Cloud Platform (GCP) |
| Data Warehouse | BigQuery |
| SDK | google-cloud-bigquery |
| Serialization | pyarrow |
| Authentication | Service Account Credentials |
| Virtual Environment | venv |
| Version Control | Git, GitHub |

---

## 3. Project Structure

```
etl-python-bigquery/
│
├── notebook/
│   └── etl_bigquery.ipynb
│
├── credentials/
│   └── service_account.json  
│
├── requirements.txt
└── README.md
```


---

## 4. ETL Workflow

### Extract  
The Iris dataset is fetched from a public repository using `pandas.read_csv()`.

### Transform  
The data is grouped by species and numerical features are aggregated using mean values.

### Load  
The transformed data is uploaded to BigQuery by:

- Initializing the BigQuery client  
- Defining dataset and table paths  
- Writing the DataFrame using `load_table_from_dataframe()`  

### Validation  
The process ends by executing a SQL query from Python to verify that the table has been loaded correctly.

---

## 5. Results

The ETL pipeline produces the table:

demo_dataset.iris_summary

Inside the GCP project:

eloquent-hangar-474417-t1

This table can later be used for dashboards, analytics, and more advanced data pipelines.

---

## 6. Author

Stefan Eduard Ababei Jorascu  
GitHub: https://github.com/Eduard-Ababei/gcp-bigquery-etl-pipeline  
This project is designed as a real-world Data Engineering practice using Python and Google Cloud BigQuery.

