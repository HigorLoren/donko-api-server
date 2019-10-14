const express = require('express');
const path = require('path');
const app = express();

app.use(express.static('build'));

app.get('/*', (req, res) => {
  res.sendFile('index.html');
});

app.listen(80, () => {
  console.log('Listening on port 80');
});
