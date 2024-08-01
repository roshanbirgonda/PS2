const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const axios = require("axios");

const app = express();
const port = 5000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

app.post("/predict", async (req, res) => {
  const { input } = req.body;

  if (!input) {
    return res.status(400).json({ error: "No input provided" });
  }
  console.log("question: " + input);
  try {
    const flaskResponse = await axios.post("http://localhost:6000/predict", {
      input,
    });
    console.log(flaskResponse.data.generated_text);
    res.json(flaskResponse.data);
  } catch (error) {
    console.error("Error generating response:", error);
    res.status(500).json({ error: "Failed to generate response" });
  }
});

app.listen(port, (x) => {
  console.log(`Server is running on http://localhost:${port}`);
});
