# AtCoder Statistics Node.js Backend

This backend collects and serves AtCoder contest statistics using Express.js.

## Setup

1. **Install dependencies:**

   ```bash
   npm install
   ```

2. **Run the server:**
   ```bash
   npm start
   ```

## API Endpoints

- `POST /collect`  
  Triggers data collection from AtCoder API and saves JSON files to `json/`.

- `GET /json/:filename`  
  Serves the generated JSON files (e.g., `stats.json`, `chart.json`, `problem_dict.json`).

## Output

Generated JSON files are saved in the `json/` directory:

- `stats.json`
- `chart.json`
- `problem_dict.json`

## Notes

- The `json/` directory will be created automatically if it does not exist.
- The backend will fetch data from the AtCoder API each time `/collect` is called.
