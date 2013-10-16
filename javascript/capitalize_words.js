var processLine = function(line){
	var words = line.split(" ");
	words.forEach(function(word, index){
		var firstLetter = word.charAt(0);
		firstLetter = firstLetter.toUpperCase();
		var characters = word.split("");
		characters[0] = firstLetter;
		words[index] = characters.join("");
	});
	return words.join(" ");
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var result = processLine(line);
  	console.log(result);
  }
});