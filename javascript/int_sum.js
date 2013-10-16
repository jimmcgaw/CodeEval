var processLine = function(line){
	
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
	var sum = 0;
  if (line != "") {
  	sum += parseInt(line, 10);
  }
  return sum;
});