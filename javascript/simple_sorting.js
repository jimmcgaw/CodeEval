var processLine = function(line){
	var floats = line.split(" ");
	for (var i = 0, len = floats.length; i < len; i++) {
		floats[i] = parseFloat(floats[i]);
	}
	floats.sort(function(a, b) {
    return a - b;
	});
	for (var i = 0, len = floats.length; i < len; i++) {
		floats[i] = floats[i].toFixed(3);
	}
	return floats.join(" ");
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var result = processLine(line);
  	console.log(result);
  }
});