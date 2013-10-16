var processLine = function(line){
	var numbers = line.split(";");
	numbers.forEach(function(number, index){
		switch (number){
			case "zero":
				numbers[index] = 0;
				break;
			case "one":
				numbers[index] = 1;
				break;
			case "two":
				numbers[index] = 2;
				break;
			case "three":
				numbers[index] = 3;
				break;
			case "four":
				numbers[index] = 4;
				break;
			case "five":
				numbers[index] = 5;
				break;
			case "six":
				numbers[index] = 6;
				break;
			case "seven":
				numbers[index] = 7;
				break;
			case "eight":
				numbers[index] = 8;
				break;
			case "nine":
				numbers[index] = 9;
				break;
			default:
				numbers[index] = 0;
				break;
		}
	});

	return numbers.join("");
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var result = processLine(line);
  	console.log(result);
  }
});