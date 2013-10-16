var processLine = function(line){
	var intersection = [];
	var firstArray = line.split(";")[0].split(",");
	var secondArray = line.split(";")[1].split(",");
	for (var i = 0, len = firstArray.length; i < len; i++) {
		var member = firstArray[i];
		if ( secondArray.indexOf(member) !== -1) {
			intersection.push(member);
		}
	}
	return intersection.join(",");
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var result = processLine(line);
  	console.log(result);
  }
});