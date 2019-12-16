const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
require('dotenv').config();
const db = require('./db');

const app = express();
app.use(cors());
app.use(bodyParser.json());



app.get("/api/dailydata", async function(req, res){
    
    let datetime = new Date();
    let date = datetime.toISOString().slice(0,10);
    date = date.replace(/-/g, "");

    let sql = `SELECT date, time, temperature FROM (SELECT date, time, temperature FROM weatherdata WHERE date=${date}) AS data ORDER BY time ASC;`;
    try{
        await db.connect();
        await db.con.query(sql, function (err, result, fields) {
            if (err) throw err;
            // console.log(result);
            res.json(result);
        });
    }catch(err){
        console.log(err);
    }finally{
        await db.close();
    }
});

app.get("/api/weatherdata", async function(req, res){

    let max = {};
    let min = {};
    let current = {};

    try{
        await db.connect();
        await db.con.query();
    }catch(err){
        console.log(err);
    }finally{
        await db.close();
    }
});

app.post("/api/data", function(req, res){


    db.con.query(sql, function (err, result, fields) {
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