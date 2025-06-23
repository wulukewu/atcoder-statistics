const { collectData } = require("../atcoder");
const { createClient } = require("@supabase/supabase-js");
const fs = require("fs");
const path = require("path");

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_ROLE_KEY
);
const BUCKET = process.env.SUPABASE_BUCKET;

exports.handler = async function (event, context) {
  try {
    const result = await collectData("/tmp");
    // Upload each file to Supabase Storage
    for (const [key, filePath] of Object.entries(result)) {
      const fileName = path.basename(filePath);
      const fileBuffer = fs.readFileSync(filePath);
      const { error } = await supabase.storage
        .from(BUCKET)
        .upload(fileName, fileBuffer, {
          upsert: true,
          contentType: "application/json",
        });
      if (error) {
        console.error(`[Supabase][ERROR] Uploading ${fileName}:`, error);
        throw error;
      }
      console.log(`[Supabase] Uploaded ${fileName} to bucket ${BUCKET}`);
    }
    return {
      statusCode: 200,
      body: JSON.stringify({
        message: "Data collected and uploaded to Supabase.",
        files: Object.keys(result),
      }),
    };
  } catch (err) {
    console.error("[Netlify][ERROR] /collect failed:", err);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: err.message }),
    };
  }
};
