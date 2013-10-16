var processLine = function(line){
	var digits = line.split("");
	var sum = 0;
	for (var i = 0, len = digits.length; i < len; i++) {
		var digit = parseInt( digits[i], 10 );
		sum += digit;
	}
	return sum;
};

var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
    	var result = processLine(line);
    	console.log(result);
    }
});