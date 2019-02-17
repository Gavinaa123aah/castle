var express = require('express');
var app = express();
var fs = require("fs");
var cors = require('cors');
app.use(cors())

app.get('/listhotels', function (req, res) {
   fs.readFile( __dirname + "/" + "hotels.json", 'utf8', function (err, data) {
       console.log( data );
       
       res.end( data );
   });
})

app.get('/hello', function (req, res) {
  // res.end("hello")
  res.json({name:1});
})

var server = app.listen(8081, function () {

  var host = server.address().address
  var port = server.address().port

  console.log("server is starting", host, port)

})