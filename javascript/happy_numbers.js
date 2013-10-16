// given string w/ number, return sum of square of digits
var digitSquareSum = function(digitsString){
	var chars = digitsString.split("");
	var sum = 0;
	for (var i = 0, len = chars.length; i < len; i++){
		var digit = parseInt(chars[i], 10);
		var square = Math.pow(digit, 2);
		sum += square;
	}
	// console.log(sum);
	return sum.toString();
};

var processLine = function(line){
	var result = digitSquareSum(line);
	var count = 0;
	while(result !== "1" && count < 1000) {
		result = digitSquareSum(result);
		count++;
	}
	if (result === "1") {
		return result;
	} else {
		return "0"
	}
};

var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
    	var result = processLine(line);
    	console.log(result);
    }
});