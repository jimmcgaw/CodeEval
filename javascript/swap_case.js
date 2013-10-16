var processLine = function(line){
	var characters = line.split("");
	characters.forEach(function(character, index){
		if (character === character.toUpperCase()) {
			characters[index] = character.toLowerCase();
		} else {
			characters[index] = character.toUpperCase();
		}
	});
	return characters.join("");
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var result = processLine(line);
  	console.log(result);
  }
});