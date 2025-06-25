const express = require("express");
const path = require("path");
const cors = require("cors"); 
const { collectData, readJsonFile, createProfileJson } = require("./atcoder");
const app = express();
const PORT = process.env.PORT || 8000;
const DATA_DIR = path.join(__dirname, "json");
const fetch = require("node-fetch"); 

console.log("[INFO] DATA_DIR is:", DATA_DIR);

app.use(cors()); 
app.use(express.json());

app.post("/collect", async (req, res) => {
  try {
    const result = await collectData(DATA_DIR);
    console.log("[INFO] Data collected and files written:", result);
    res.json({ message: "Data collected.", files: result });
  } catch (err) {
    console.error("[ERROR] /collect failed:", err);
    res.status(500).json({ error: err.message });
  }
});

app.get("/json/:filename", (req, res) => {
  const data = readJsonFile(DATA_DIR, req.params.filename);
  if (!data) {
    console.error(
      `[ERROR] File not found: ${req.params.filename} in ${DATA_DIR}`
    );
    return res.status(404).send("File not found");
  }
  res.type("json").send(data);
});


// Proxy for AtCoder user ac_rank
app.get("/atcoder/user/ac_rank/:user", async (req, res) => {
  const user = req.params.user;
  const url = `https://kenkoooo.com/atcoder/atcoder-api/v3/user/ac_rank?user=${encodeURIComponent(user)}`;
  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error("Failed to fetch ac_rank");
    const data = await response.json();
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Proxy for AtCoder user rated_point_sum_rank
app.get("/atcoder/user/rated_point_sum_rank/:user", async (req, res) => {
  const user = req.params.user;
  const url = `https://kenkoooo.com/atcoder/atcoder-api/v3/user/rated_point_sum_rank?user=${encodeURIComponent(user)}`;
  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error("Failed to fetch rated_point_sum_rank");
    const data = await response.json();
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.get("/atcoder/profile/:user", async (req, res) => {
  const user = req.params.user;
  try {
    const profile = await createProfileJson(DATA_DIR, user);
    res.json(profile);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  // Auto-trigger data collection on server start
  const http = require("http");
  function triggerCollect() {
    http
      .request(
        {
          hostname: "localhost",
          port: PORT,
          path: "/collect",
          method: "POST",
        },
        (res) => {
          console.log(`Auto-collect status: ${res.statusCode}`);
        }
      )
      .on("error", (err) => {
        console.error("Auto-collect error:", err.message);
      })
      .end();
  }
  triggerCollect(); // Initial collect on start
  setInterval(triggerCollect, 3 * 60 * 60 * 1000); // Every 3 hours
});
