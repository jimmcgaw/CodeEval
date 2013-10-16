
		
var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
    	var numbers = line.split("");
    	
    	console.log();
    }
});