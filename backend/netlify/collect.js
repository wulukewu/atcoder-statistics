const { collectData } = require("../atcoder");

exports.handler = async function (event, context) {
  try {
    await collectData("/tmp");
    return {
      statusCode: 200,
      body: JSON.stringify({ message: "Data collected." }),
    };
  } catch (err) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: err.message }),
    };
  }
};
