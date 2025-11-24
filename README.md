# ETL Pipeline with Python and Google BigQuery

Este proyecto implementa un flujo ETL completo utilizando Python, pandas y Google BigQuery.  
Demuestra la integración entre un entorno local de análisis de datos y un data warehouse en la nube, replicando un caso práctico real de ingeniería de datos.

---

## 1. Descripción general

El pipeline ejecuta las tres fases principales del proceso ETL:

**Extract:** lectura de un dataset público desde un repositorio remoto.  
**Transform:** limpieza, agregación y cálculo de métricas con pandas.  
**Load:** carga del resultado transformado en una tabla de Google BigQuery mediante la API oficial.

Este proyecto sirve como referencia práctica para conectar Python con Google Cloud Platform gestionando credenciales, clientes, datasets y consultas SQL.

---

## 2. Tecnologías utilizadas

| Categoría | Herramienta |
|----------|-------------|
| Lenguaje | Python 3.x |
| Data Wrangling | pandas |
| Cloud Platform | Google Cloud Platform (GCP) |
| Data Warehouse | BigQuery |
| SDK | google-cloud-bigquery |
| Serialización | pyarrow |
| Autenticación | Service Account Credentials |
| Entorno | venv |
| Control de versiones | Git, GitHub |

---

## 3. Estructura del proyecto

\`\`\`
etl-python-bigquery/
│
├── notebook/
│   └── etl_bigquery.ipynb
│
├── credentials/
│   └── service_account.json   (no subir a GitHub)
│
├── requirements.txt
└── README.md
\`\`\`

---

## 4. Flujo ETL

### Extract  
Se obtiene el dataset Iris desde un repositorio abierto utilizando `pandas.read_csv()`.

### Transform  
Se agrupan las observaciones por especie y se calculan medias de las columnas numéricas.

### Load  
El resultado se carga en BigQuery mediante:

- inicialización del cliente  
- creación de dataset y tabla  
- carga con `load_table_from_dataframe()`  

### Validación  
El pipeline finaliza ejecutando una consulta SQL desde Python para comprobar que la tabla se ha cargado correctamente.

---

## 5. Resultados

El flujo ETL genera la tabla:

demo_dataset.iris_summary


Dentro del proyecto de GCP:

eloquent-hangar-474417-t1


Esta tabla puede utilizarse posteriormente en dashboards, análisis o pipelines avanzados.

---

## 6. Autor

Stefan Eduard Ababei Jorascu
Github: https://github.com/Eduard-Ababei/Proyecto-etl-python-bigquery
Proyecto orientado a prácticas reales de Data Engineering con Python y Google Cloud.
