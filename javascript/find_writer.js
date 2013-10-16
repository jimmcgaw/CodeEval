var processLine = function(line){
	var characters = line.split("| ")[0];
	var positions = line.split("| ")[1].split(" ");

	var authorName = [];

	positions.forEach(function(position, index){
		authorName.push( characters[position-1] );
	});
	return authorName.join("");
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var result = processLine(line);
  	console.log(result);
  }
});