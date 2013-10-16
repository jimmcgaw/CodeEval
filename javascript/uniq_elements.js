var processLine = function(line){
	var elements = line.split(",");
	var distinct = [];
	for (var i = 0, len = elements.length; i < len; i++) {
		var element = elements[i];
		if ( distinct.indexOf(element) === -1 ) {
			distinct.push(element);
		}
	}
	return distinct.join(",");
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var result = processLine(line);
  	console.log(result);
  }
});