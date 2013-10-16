var processLine = function(line){
	var characters = line.split("");
	var firstChar = characters[0];
	var period = 0;
	characters.forEach(function(character, index){
		if (index !== 0 && period === 0 && firstChar === character) {
			period = index;
		}
	});

	return period;
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var result = processLine(line);
  	console.log(result);
  }
});