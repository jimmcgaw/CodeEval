var processLine = function(line){
	var digits = line.split(",");
	var x = parseInt(digits[0], 10);
	var n = parseInt(digits[1], 10);
	var multiple = 1;
	while ( (n * multiple) < x){
		multiple++;
	}
	return n * multiple;
};

var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
    	var result = processLine(line);
    	console.log(result);
    }
});