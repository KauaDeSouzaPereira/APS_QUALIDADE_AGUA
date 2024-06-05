var express = require('express');
var mysql = require('mysql');
var app = express();

var con = mysql.createConnection({
  host: "localhost",
  user: "aps",
  password: "7654321",
  database: "aps_qualidade_agua"
});

app.get('/sensores', function (req, res) {
  con.query("SELECT * FROM sensores", function (err, result, fields) {
    if (err) throw err;
    res.json(result);
  });
});

app.listen(3000, function () {
  console.log('App listening on port 3000!');
});
