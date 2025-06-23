const express = require("express");
const path = require("path");
const cors = require("cors"); // <-- add this
const { collectData, readJsonFile } = require("./atcoder");
const app = express();
const PORT = process.env.PORT || 8000;
const DATA_DIR = path.join(__dirname, "json");

app.use(cors()); // <-- add this, needs npm install cors
app.use(express.json());

app.post("/collect", async (req, res) => {
  try {
    await collectData(DATA_DIR);
    res.json({ message: "Data collected." });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.get("/json/:filename", (req, res) => {
  const data = readJsonFile(DATA_DIR, req.params.filename);
  if (!data) return res.status(404).send("File not found");
  res.type("json").send(data);
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
