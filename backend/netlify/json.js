const { createClient } = require("@supabase/supabase-js");

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_ROLE_KEY
);
const BUCKET = process.env.SUPABASE_BUCKET;

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
  // Download file from Supabase Storage
  const { data, error } = await supabase.storage
    .from(BUCKET)
    .download(filename);
  if (error || !data) {
    console.error(`[Supabase][ERROR] Downloading ${filename}:`, error);
    return { statusCode: 404, body: "File not found" };
  }
  // Read the stream into a string
  const buffer = await data.arrayBuffer();
  const json = Buffer.from(buffer).toString("utf-8");
  console.log(`[Supabase] Served file: ${filename} from bucket ${BUCKET}`);
  return {
    statusCode: 200,
    headers: { "Content-Type": "application/json" },
    body: json,
  };
};
