var processLine = function(line){
	var characters = line.split(" ");
	var charCounts = {};
	characters.forEach(function(character, index){
		if (charCounts[character]) {
			charCounts[character]++;
		} else {
			charCounts[character] = 1;
		}
	});

	var winningDigit = 0;

	for (character in charCounts){
		if (charCounts[character] === 1) {
			if (charCounts[character] > winningDigit || winningDigit === 0){
				winningDigit = character;	
			}
			
		}
	}
	var winningPosition = characters.indexOf(winningDigit.toString())+1;
	if (winningPosition > 0){
		return winningPosition;
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