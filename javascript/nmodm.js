var processLine = function(line){
	var n = parseInt(line.split(",")[0], 10);
	var m = parseInt(line.split(",")[1], 10);
	if (m > n) {
		return n;
	}

	var multiple = 1;
	while ( (n - (m*multiple)) > m ){
		multiple++;
	}

	return n - (m*multiple);

};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var result = processLine(line);
  	console.log(result);
  }
});