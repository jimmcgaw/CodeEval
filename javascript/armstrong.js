var processLine = function(line){
	var n_digit = line.length;
	var characters = line.split("");
	var number = parseInt(line, 10);
	var sum = 0;
	for (var i = 0, len = characters.length; i < len; i++) {
		 var digit = parseInt(characters[i], 10);
		 sum += Math.pow(digit, n_digit);
	};
	if (sum.toString() === line) {
		return "True";
	} else {
		return "False";
	}
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var result = processLine(line);
  	console.log(result);
  }
});