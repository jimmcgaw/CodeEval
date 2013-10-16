var processLine = function(line){
	var elements = line.split(" : ")[0].split(" ");
	var swaps = line.split(" : ")[1].split(", ");

	swaps.forEach(function(swap, index){
		var firstIndex = parseInt(swap.split("-")[0], 10);
		var secondIndex = parseInt(swap.split("-")[1], 10);
		var firstValue = elements[firstIndex];
		var secondValue = elements[secondIndex];

		elements[firstIndex] = secondValue;
		elements[secondIndex] = firstValue;
	});

	return elements.join(" ");
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var result = processLine(line);
  	console.log(result);
  }
});