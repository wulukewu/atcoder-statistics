const { readJsonFile } = require("../atcoder");

exports.handler = async function (event, context) {
  // Support both ?filename=chart.json and /json/chart.json
  let filename =
    event.queryStringParameters && event.queryStringParameters.filename;
  if (!filename && event.path) {
    // Extract filename from path, e.g. /.netlify/functions/json/chart.json
    const match = event.path.match(/\/json\/?(.+)/);
    if (match && match[1]) {
      filename = match[1];
    }
  }
  if (!filename) {
    console.error("[Netlify][ERROR] Missing filename parameter");
    return { statusCode: 400, body: "Missing filename parameter" };
  }
  const data = readJsonFile("/tmp", filename);
  if (!data) {
    console.error(`[Netlify][ERROR] File not found: ${filename} in /tmp`);
    return { statusCode: 404, body: "File not found" };
  }
  console.log(`[Netlify] Serving file: ${filename} from /tmp`);
  return {
    statusCode: 200,
    headers: { "Content-Type": "application/json" },
    body: data,
  };
};
