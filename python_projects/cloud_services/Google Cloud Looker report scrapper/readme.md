# Looker Report Mapper

This tool scans all dashboards in Looker and generates a **report of reports** — a structured dataset containing:

- All dashboards and their elements
- All fields used in tables (including renamed fields via `series_labels`)
- All dashboard filters and their mapped fields

## Purpose

With hundreds of reports and thousands of fields, it's often difficult to know:

- Where a specific field is being used (e.g., `employee date of birth`)
- Whether a field is renamed in a report (e.g., `dob` → `Birth Date`)
- Which filters exist and what fields they control

This tool solves that by creating a centralized view of all report structure and metadata.

## Output

- `df1`: Full metadata per field per dashboard element
- `df2`: Field-to-label mapping
- `df3`: Dashboard filters and their target fields

The result can be searched or filtered to answer questions like:
- *Which dashboards use the field `employee.date_of_birth`?*
- *Where is `Birth Date` shown as a column?*
- *What filters exist for `hire_date`?*

## Requirements

- Looker SDK
- `pandas`
- `tqdm`

## Notes

- Dashboards without valid queries or `series_labels` are skipped
- Can be customized to target specific dashboards or explore all

