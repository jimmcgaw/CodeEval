var processLine = function(line){
	line = line.replace(") (", "|").replace("(", "").replace(")", "");
	var pair_one = line.split("|")[0];
	var pair_two = line.split("|")[1];

	var x1 = parseInt( pair_one.split(", ")[0]);
	var y1 = parseInt( pair_one.split(", ")[1]);
	var x2 = parseInt( pair_two.split(", ")[0]);
	var y2 = parseInt( pair_two.split(", ")[1]);

	return Math.sqrt( Math.pow(x2-x1, 2) + Math.pow(y2-y1, 2) );

};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var result = processLine(line);
  	console.log(result);
  }
});