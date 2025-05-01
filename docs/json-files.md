# AtCoder Statistics JSON Files

The `main.py` script generates three JSON files that are stored in the `web-page/json/` directory:

## 1. `problem_id_to_contest_id.json`

This file contains a mapping of problem IDs to their corresponding contest IDs. Some problems may appear in multiple contests.

Structure:
```json
{
  "abc123_a": ["abc123"],
  "abc124_b": ["abc124"],
  "arc089_a": ["abc086", "arc089"]
}