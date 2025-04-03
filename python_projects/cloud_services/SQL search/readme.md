# SQL Search Utility

A flexible, regex-based notebook utility to **search across SQL files** for keywords, conditions, and patterns. Designed to assist with auditing, debugging, or investigating SQL logic across large codebases.

---

## Features

- 🔍 **Search multiple `.sql` files** at once using `glob` patterns
- 🧠 **Flexible search modes**: match one keyword, both, either, or only one of them
- 🎯 **Approximate or strict matching** using regex boundaries
- ✂️ **Comment-aware**: supports ignoring commented-out lines
- 📄 **Result output to CSV** for further analysis
- 📌 **Ignore list support** for skipping known files
- 🎨 **Styled results** with keyword highlighting

---

## Example Use Case

Want to know which queries reference a particular field (`isMigrated`) or a specific plan year (`20245`)?

```python
word_1 = "isMigrated"
word_2 = "20245"
method = "any"
path = "queries/**/*.sql"
approximate = True

results = sql_search(word_1, word_2, method, approximate, path)
results.to_csv("matches.csv")
```

This will search all SQL files under `queries/`, and return lines containing either keyword.

---

## Search Modes

| Method         | Description                                       |
|----------------|---------------------------------------------------|
| `both`         | File must contain **both** `word_1` and `word_2`  |
| `any`          | File must contain **either** `word_1` or `word_2` |
| `word_1`       | File must contain `word_1`                        |
| `word_2`       | File must contain `word_2`                        |
| `word_1_only`  | File must contain `word_1` but **not** `word_2`   |

---

## Parameters

- `word_1`, `word_2`: keywords to search for
- `method`: search logic (see above)
- `approximate`: whether to do a soft match or word-boundary match
- `path`: glob path to search files in (`queries/**/*.sql` by default)
- `with_comments`: (currently unused) to control comment stripping
- `ignorelist`: list of files to exclude from the result

---

## Output

- Matching lines are returned as a pandas DataFrame:
  - `file`: file path
  - `line_number`: line index in file
  - `line`: matching line
  - `match`: which word was matched
- DataFrame can be styled and exported to CSV

---

## Requirements

- Python 3.x
- pandas
- re
- glob
- Jupyter Notebook

Install requirements:
```bash
pip install pandas
```
