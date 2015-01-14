var fb = require('./index.js');
var datadir = process.argv[2];
console.log(fb.describe({from:datadir}));