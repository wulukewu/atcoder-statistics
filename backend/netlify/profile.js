const { createProfileJson } = require("../atcoder");
const path = require("path");

const DATA_DIR = "/tmp"; // Netlify functions use /tmp for temp storage

exports.handler = async function (event, context) {
  // Support both /profile/:user and /profile?user=xxx
  let user = null;
  if (event.queryStringParameters && event.queryStringParameters.user) {
    user = event.queryStringParameters.user;
  } else if (event.path) {
    // Extract username from path, e.g. /.netlify/functions/profile/username
    const match = event.path.match(/\/profile\/?([^\/\?]+)/);
    if (match && match[1]) {
      user = match[1];
    }
  }
  if (!user) {
    return {
      statusCode: 400,
      body: JSON.stringify({ error: "Missing user parameter" }),
    };
  }
  try {
    const profile = await createProfileJson(DATA_DIR, user);
    return {
      statusCode: 200,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(profile),
    };
  } catch (err) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: err.message }),
    };
  }
};
