# AtCoder Statistics JSON Documentation

This document provides detailed information about the JSON data structures used in the AtCoder Statistics project, including both the external API data and the generated JSON files.

## External API Data

The project fetches data from three AtCoder API endpoints:

### 1. Contest Problem JSON

**Source:** `https://kenkoooo.com/atcoder/resources/contest-problem.json`

This API provides information about which problems belong to which contests.

**Structure:**
```json
[
  {
    "contest_id": "abc123",
    "problem_id": "abc123_a",
    "problem_index": "A"
  },
  {
    "contest_id": "abc123",
    "problem_id": "abc123_b",
    "problem_index": "B"
  }
]