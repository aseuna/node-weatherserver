var mysql = require('mysql');
require('dotenv').config();

module.exports = {
    config: {
        host: process.env.DB_HOST,
        user: process.env.DB_USER,
        password: process.env.DB_PASSWORD,
        database: process.env.DB_NAME
    },
    con: null,
    connect: async function(){
        this.con = mysql.createConnection(this.config);
        this.con.connect(function(err) {
            if (err) throw err;
        });
    },
    close: async function(){
        try{
            this.con.end();
            this.con = null;
            console.log("connection status:");
            console.log(this.con);
        }
        catch(err){
            console.log(err);
        }
    }
}