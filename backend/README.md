# AtCoder Statistics Backend

This backend collects and serves AtCoder contest statistics. It is designed for both local/server use (Express.js) and serverless deployment (Netlify Functions), with all core logic shared in a single module.

## Structure

```
backend/
  atcoder.js         # Core logic (fetch/process/save/read)
  index.js           # Express server (local/server use)
  netlify/
    collect.js       # Netlify Function: POST /.netlify/functions/collect
    json.js          # Netlify Function: GET /.netlify/functions/json?filename=...
```

## Setup (Express.js)

1. **Install dependencies:**
   ```bash
   npm install
   ```
2. **Run the server:**
   ```bash
   npm start
   ```

## API Endpoints (Express.js)

- `POST /collect`  
  Triggers data collection from AtCoder API and saves JSON files to `json/`.
- `GET /json/:filename`  
  Serves the generated JSON files (e.g., `stats.json`, `chart.json`, `problem_dict.json`).

## Output

Generated JSON files are saved in the `json/` directory:

- `stats.json`
- `chart.json`
- `problem_dict.json`

## Example curl Commands

### For Express.js (local/server)

- Trigger data collection:
  ```bash
  curl -X POST http://localhost:3000/collect
  ```
- Fetch a JSON file (e.g., stats.json):
  ```bash
  curl http://localhost:3000/json/stats.json
  ```

### For Netlify Functions (deployed)

- Trigger data collection:
  ```bash
  curl -X POST https://<your-netlify-site>.netlify.app/.netlify/functions/collect
  ```
- Fetch a JSON file (e.g., stats.json):
  ```bash
  curl "https://<your-netlify-site>.netlify.app/.netlify/functions/json?filename=stats.json"
  ```

---

## Netlify Functions Usage

Netlify will use the functions in `backend/netlify/` as serverless endpoints. Make sure your `netlify.toml` contains:

```
[build]
  functions = "backend/netlify"
```

### Endpoints (Netlify Functions)

- `POST /.netlify/functions/collect`  
  Fetches and processes AtCoder data, saves JSON files to `/tmp`.
- `GET /.netlify/functions/json?filename=stats.json`  
  Serves the generated JSON files (`stats.json`, `chart.json`, `problem_dict.json`).

**Note:** Netlify Functions are stateless. Files are stored in `/tmp` and are not persistent between function invocations or deploys.

## Development Notes

- All AtCoder logic is in `atcoder.js`. Both Express and Netlify Functions use this.
- Update logic in one place for both environments.
