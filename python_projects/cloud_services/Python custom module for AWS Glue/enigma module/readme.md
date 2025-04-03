# Enigma - AWS Glue Utilities

Enigma is a custom Python module built to streamline and standardize development on AWS Glue. It provides reusable utility functions for working with Spark SQL, UUID generation, S3 CSV exports, secrets management, and connecting to external databases (like PostgreSQL and BigQuery).

## 🔧 Features

### Spark + Glue Helpers
- **`sparkSqlQuery_`**: Run SQL queries on a set of mapped DynamicFrames.
- **`add_field_`**: Add a new UUIDv7 column to a DynamicFrame and optionally sort it.
- **`read_table_`**: Read from AWS Glue Data Catalog or BigQuery based on environment config.
- **`write_table_`**: Write to Glue tables with column comparison and logging.
- **`write_csv`**: Export data to S3 as CSV with schema checks and S3 folder validation.

### Secrets + Database
- **`get_secret`**: Fetch secrets from AWS Secrets Manager and return them as a dictionary.
- **`connect_to_db`**: Connect to a PostgreSQL database using credentials pulled from Secrets Manager.

## 🛠 PowerShell Build Script

A script is included to automate packaging and deployment:

1. Checks syntax of all `.py` files.
2. Builds the wheel file.
3. Uploads it to a designated S3 path.
4. Verifies the upload by checking file metadata.
5. Keeps the terminal open for review.

## ⚠️ Error Handling

Quasar includes built-in error handling to make debugging and failure tracing easier:

- Raises descriptive `ValueError`s when critical arguments like `glueContext` are missing.
- Catches and prints clear messages for schema mismatches during table writes.
- Validates environment inputs and catches invalid configurations (e.g. unknown database or table names).
- In `write_csv`, detects non-CSV files in the target S3 path and stops to prevent accidental overwrites.
- All exceptions in secret and DB connection logic are printed and re-raised for visibility in logs.

This helps ensure data pipelines fail loudly and informatively rather than silently skipping steps.

## 📦 Usage

To use this module in your AWS Glue job:

```python
from enigma import sparkSqlQuery_, read_table_, write_csv, connect_to_db

df = read_table_('dev', 'my_table', glueContext)
write_csv(df, path='exports/my_table/')
```

To connect to a database:
```python
conn = connect_to_db('env_migrate')
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM users")
print(cursor.fetchone())
conn.close()
```

## 📁 Directory Structure

```
project/
│
├── enigma/               # Python module with utility functions
├── dist/                 # Output directory for the built wheel
├── build_script.ps1      # PowerShell automation for packaging and upload
├── setup.py              # Standard Python packaging config
└── README.md             # You're here
```

## ✅ Requirements
- Python 3.x
- AWS CLI configured
- boto3, pyspark, psycopg2 installed
- AWS Glue job environment or local setup for testing
