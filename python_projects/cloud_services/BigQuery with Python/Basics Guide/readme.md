# BigQuery with Python: Basic Operations Guide

This guide provides simple, ready-to-use examples for interacting with **Google BigQuery** using Python. It covers essential operations such as connecting to BigQuery, reading and writing tables, copying and deleting tables, and accessing table metadata and view definitions.

---

## Covered Operations

### 1. Connect to BigQuery

Establish a client connection using the `google-cloud` library.

### 2. Read Table

Query and load a BigQuery table into a Pandas DataFrame.

### 3. Write Table

Write a DataFrame to a BigQuery table with support for different write modes (`WRITE_APPEND`, `WRITE_TRUNCATE`, etc.).

### 4. Copy Table

Duplicate an existing BigQuery table to another location (within the same project or across datasets).

### 5. Delete Table

Programmatically delete a BigQuery table.

### 6. Get Table Schema

Retrieve and inspect the schema (column names and data types) of a table.

### 7. Get View Query

Extract the SQL definition of a BigQuery view.

---

## Requirements

- Python 3.6+
- `google-cloud-bigquery`
- Valid Google Cloud credentials with access to BigQuery

Install the required library:

```bash
pip install google-cloud-bigquery
```

---

## Authentication

Make sure your environment is authenticated:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account.json"
```
