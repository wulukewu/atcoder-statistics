const { collectData } = require("../atcoder");

exports.handler = async function (event, context) {
  try {
    const result = await collectData("/tmp");
    console.log("[Netlify] Data collected and files written:", result);
    return {
      statusCode: 200,
      body: JSON.stringify({ message: "Data collected.", files: result }),
    };
  } catch (err) {
    console.error("[Netlify][ERROR] /collect failed:", err);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: err.message }),
    };
  }
};
