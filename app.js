var express = require('express');   
var app = express();
var bodyParser = require('body-parser')
app.set('view engine','ejs');

app.use(bodyParser.urlencoded({extended: true}));

app.get('/', function(req,res){
    res.render('home');
    console.log(req.body);
});


app.listen(3000, () => console.log('Example app listening on port 3000!'))