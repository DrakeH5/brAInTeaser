const express = require("express")
const app = express()
const cors = require("cors");
app.use(cors());
var bodyParser = require('body-parser')

app.get("/", (req, res) => {
  res.json("Welcome to the backend")
})

app.post("/generateQuestions", bodyParser.json(), (req, res) => {
  res.json(req.body.input)
})


app.listen(5000, () => { console.log("Server started on port 5000") })



