# AtCoder Statistics Backend

This backend collects and serves AtCoder contest statistics. It is designed for both local/server use (Express.js) and serverless deployment (Netlify Functions), with all core logic shared in a single module. For Netlify deployment, it uses Supabase Storage for persistent file storage.

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
   (The server will run on port 8000 by default)

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
  curl -X POST http://localhost:8000/collect
  ```
- Fetch a JSON file (e.g., chart.json):
  ```bash
  curl http://localhost:8000/json/chart.json
  ```

### For Netlify Functions (deployed with Supabase Storage)

- Trigger data collection and upload to Supabase:
  ```bash
  curl -X POST https://<your-netlify-site>.netlify.app/.netlify/functions/collect
  ```
- Fetch a JSON file (e.g., chart.json):
  ```bash
  curl "https://<your-netlify-site>.netlify.app/.netlify/functions/json?filename=chart.json"
  # or
  curl "https://<your-netlify-site>.netlify.app/.netlify/functions/json/chart.json"
  ```

---

## Netlify Functions Usage with Supabase Storage

Netlify will use the functions in `backend/netlify/` as serverless endpoints. Make sure your `netlify.toml` contains:

```
[build]
  functions = "backend/netlify"
  publish = "frontend/build"  # if you have a frontend
```

### Endpoints (Netlify Functions)

- `POST /.netlify/functions/collect`  
  Fetches and processes AtCoder data, saves JSON files to Supabase Storage.
- `GET /.netlify/functions/json?filename=chart.json`  
  Serves the generated JSON files (`stats.json`, `chart.json`, `problem_dict.json`) from Supabase Storage.

**Note:** Netlify Functions are stateless. Files are stored in Supabase Storage for persistence.

---

## Supabase Storage Setup for Netlify Backend

1. **Create a Supabase account and project:**
   - https://app.supabase.com/
2. **Create a storage bucket:**
   - Go to "Storage" → "New bucket" (e.g., `atcoder-json`).
   - Set to public or private as needed.
3. **Get your API keys:**
   - Go to "Project Settings" → "API".
   - Copy your `Project URL` (e.g., `https://xxxx.supabase.co`).
   - Copy your `service_role` key (for backend uploads).
4. **Set these as environment variables in Netlify:**
   - `SUPABASE_URL` = your Project URL
   - `SUPABASE_SERVICE_ROLE_KEY` = your service_role key
   - `SUPABASE_BUCKET` = your bucket name (e.g., `atcoder-json`)
   - **If you are deploying the frontend to Netlify, also set:**
     - `REACT_APP_API_BASE=/.netlify/functions`
     - (This tells your React frontend to use the Netlify Functions as the backend API)
5. **Deploy your site to Netlify.**

---

## Development Notes

- All AtCoder logic is in `atcoder.js`. Both Express and Netlify Functions use this.
- Update logic in one place for both environments.
- For persistent storage on Netlify, Supabase Storage is used.
