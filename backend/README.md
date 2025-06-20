# AtCoder Statistics FastAPI Backend

This backend collects and serves AtCoder contest statistics using FastAPI.

## Setup

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the server:**
   ```bash
   uvicorn app:app --reload
   ```

## API Endpoints

- `POST /collect`  
  Triggers data collection from AtCoder API and saves JSON files to `json/`.

- `GET /json/{filename}`  
  Serves the generated JSON files (e.g., `stats.json`, `chart.json`, `problem_dict.json`).

## Output

Generated JSON files are saved in the `json/` directory:

- `stats.json`
- `chart.json`
- `problem_dict.json`

## Automatic Updates

- The backend automatically fetches and updates the JSON files every 3 hours in the background.
- You can still manually trigger an update at any time by calling the `/collect` endpoint.

## Notes

- The `json/` directory will be created automatically if it does not exist.
- The backend will fetch data from the AtCoder API each time `/collect` is called or every 3 hours automatically.
