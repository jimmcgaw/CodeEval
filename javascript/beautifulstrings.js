var processLine = function(line){
	line = line.toLowerCase();
	var characters = line.split("");
	var letters = [];

	for (var i = characters.length - 1; i >= 0; i--) {
		if (characters[i].match(/[a-zA-Z]/)){
			letters.push(characters[i]);
		}
	};

	var charCounts = {};

	for (var i = letters.length - 1; i >= 0; i--) {
		var letter = letters[i];
		if (charCounts[letter]){
			charCounts[letter]++
		} else {
			charCounts[letter] = 1;
		}
	};

	var score = 0;
	var counts = [];
	for (letter in charCounts){
		counts.push(charCounts[letter]);
	}
	counts = counts.sort().reverse();

	for (var i = 0, len = counts.length; i < len; i++) {
		score += counts[i] * (26 - i);
	};

	return score.toString();
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var result = processLine(line);
  	console.log(result);
  }
});