
# BigQuery View & Table Query Extractor

This script automates the extraction of **SQL definitions** from both **views** and **scheduled queries** (tables with recently executed queries) across BigQuery datasets.

---

## Features

- 📥 **Extract View Definitions**  
  Downloads the SQL query behind each view into a local `.sql` file.

- 📥 **Extract Latest Table Queries**  
  Retrieves the most recent successful query used to create each table (based on scheduled queries in `INFORMATION_SCHEMA.JOBS_BY_PROJECT`).

- 📁 **Organized Folder Structure**  
  Saves queries under `queries/{dataset}/` with clear naming for views and tables.

---

## How It Works

1. Iterates over a list of datasets (`subsets`).
2. For each dataset:
   - Checks each table:
     - If it's a **view**, saves its `view_query` as `{view_id}.sql`.
     - If it's a **regular table**, stores the table name for further analysis.
3. Queries BigQuery’s `INFORMATION_SCHEMA.JOBS_BY_PROJECT` to find the **most recent successful query** for each non-view table.
4. Saves those queries as `t_{table_id}.sql`.

---

## Example Output Structure

```
queries/
├── reports/
│   ├── user_activity.sql       # A view
│   ├── t_sales_data.sql        # A table (scheduled query)
├── manual/
│   ├── product_summary.sql     # A view
│   ├── t_logs.sql              # A table (scheduled query)
```

---

## Requirements

- Python 3.x
- Google Cloud BigQuery client:
  ```bash
  pip install google-cloud-bigquery pandas
  ```
- Authenticated with a service account or `gcloud auth application-default login`

---

## Configuration

Inside the script:

- `subsets = ['reports', 'manual']`: List of datasets to process.
- `root = 'queries'`: Base folder where `.sql` files will be saved.

---

## Notes

- Views are saved with their original `table_id`.
- Tables from scheduled queries are saved as `t_{table_id}.sql`.
- The script will skip any dataset that doesn't exist or is inaccessible.

