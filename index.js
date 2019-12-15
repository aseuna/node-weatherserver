const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
require('dotenv').config();
const db = require('./db');

const app = express();
app.use(cors());
app.use(bodyParser.json());



app.get('/api/dailydata', function(req, res){
    
    var datetime = new Date();
    var date = datetime.toISOString().slice(0,10);
    var date = date.replace(/-/g, "");

    var sql = "SELECT date, time, temperature FROM (SELECT date, time, temperature FROM weatherdata WHERE date=?) AS data ORDER BY time ASC;";

    db.query(sql,[date], function (err, result, fields) {
        if (err) throw err;
        //console.log(result);
        res.json(result);
    });
});

app.post("/api/data", function(req, res){


    db.query(sql, function (err, result, fields) {
        if (err) throw err;
        console.log(result);
        //res.json(result);
    });
});


var server = app.listen(process.env.PORT, function() {
    var host = server.address().address;
    var port = server.address().port;
    console.log('Example app listening at http://%s:%s', host, port);

  });