var processLine = function(line){
	if ( parseInt(line, 10) % 2 === 0) {
		return "1";
	} else {
		return "0";
	}
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var result = processLine(line);
  	console.log(result);
  }
});