# Glue Notebook Modifier

This project demonstrates how to automate **bulk modifications of AWS Glue Studio notebooks** using a script-driven approach. The `glue_modifier.ipynb` notebook showcases how repetitive, manual edits - such as modifying `%connections` directives - can be streamlined across multiple Glue jobs without opening or editing them individually.

## Why This Matters

AWS Glue Studio notebooks are often environment-specific, and editing them at scale (across development, staging, and production) can become tedious and error-prone. This utility enables efficient, consistent, and automated transformations across many notebooks in one pass.

---

## Key Features

- 🔁 **Bulk modification of Glue notebooks**  
  Modify hundreds of `.ipynb` Glue notebooks at once.

- 🔍 **Pattern-based transformation**  
  Locate and replace `%connections` lines dynamically based on the content.

- ⚙️ **Environment parameterization**  
  Replace hardcoded targets like `target_env_prod` with templated versions like `target_env_test`.

- 🧹 **Optional pre-cleaning**  
  Remove commented lines before processing to avoid accidental matches.

- 📥📤 **Supports S3 workflows**  
  Download original notebooks from S3 and upload the modified versions to replace the old one.

---

## How It Works

The script:

1. Loads a list of notebook files (`step_etls`) from a source folder.
2. For each notebook:
   - Reads the content.
   - Removes comment lines.
   - Finds and rewrites the `%connections` line(s).
   - Logs what was changed.
3. Writes the updated notebook to a results folder.
4. Optionally, uploads the modified notebooks to S3.

### Edge Case Handling

- ❗ Multiple `%connections` lines in one notebook? Skipped and flagged.
- ❗ No `%connections` line? Skipped and logged.
- ✅ Successful edits are clearly logged per file.
- ❗ Will not upload if the modification failed, to prevent uploading a corrupted or unmodified notebook.

---

## Extendability

This framework can be extended to support:

- Renaming functions or imports
- Injecting logging or debug cells
- Enforcing coding standards across all notebooks
- Any other regex-based transformations

