var processLine = function(line){
	var firstList = line.split(" | ")[0].split(" ");
	var secondList = line.split(" | ")[1].split(" ");

	var results = [];
	firstList.forEach(function(firstChar, index){
		var firstDigit = parseInt(firstChar, 10);
		var secondDigit = parseInt(secondList[index], 10);
		results.push(firstDigit * secondDigit);
	});
	return results.join(" ");
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var result = processLine(line);
  	console.log(result);
  }
});