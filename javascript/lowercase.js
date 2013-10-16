var processLine = function(line){
	return line.toLowerCase();
};

var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
    	var result = processLine(line);
    	console.log(result);
    }
});