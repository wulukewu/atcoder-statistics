const { readJsonFile } = require("../atcoder");

exports.handler = async function (event, context) {
  const filename =
    event.queryStringParameters && event.queryStringParameters.filename;
  if (!filename) return { statusCode: 400, body: "Missing filename parameter" };
  const data = readJsonFile("/tmp", filename);
  if (!data) return { statusCode: 404, body: "File not found" };
  return {
    statusCode: 200,
    headers: { "Content-Type": "application/json" },
    body: data,
  };
};

