var processLine = function(line){
	var elements = line.split(",");
	var words = [];
	var digits = [];
	elements.forEach(function(element, index){
			var digit = parseInt(element, 10);
			if ( isNaN(digit) ){
				words.push(element);
			} else {
				digits.push(digit);
			}
	});
	if (digits.length === 0) {
		return words.join(",");
	}
	if (words.length === 0) {
		return digits.join(",");
	}
	return words.join(",") + "|" + digits.join(",");
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var result = processLine(line);
  	console.log(result);
  }
});