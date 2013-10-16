var processLine = function(line){
	var string = line.split(",")[0];
	var character = line.split(",")[1];
	return string.lastIndexOf(character);
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var result = processLine(line);
  	console.log(result);
  }
});