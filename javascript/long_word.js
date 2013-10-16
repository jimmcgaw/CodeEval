var processLine = function(line){
	var words = line.split(" ");
	var longest = 0;
	var longWord = "";
	words.forEach(function(word,index){
		if (word.length > longest){
			longest = word.length;
			longWord = word;
		}
	});
	return longWord;
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var result = processLine(line);
  	console.log(result);
  }
});