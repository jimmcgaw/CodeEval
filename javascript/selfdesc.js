var processLine = function(line){
	var isSelfDescribing = true;
	
	var characters = line.split("");
	for (var position = 0, len = characters.length; position < len; position++) {
		var currentChar = characters[position]; // '2'
		var digit = parseInt(currentChar,10);  // 2

		var count = 0;
		for (var innerIndex = 0, len = characters.length; innerIndex < len; innerIndex++) {
			var innerChar = characters[innerIndex];
			if (position.toString() === innerChar) {
				count++;
			}
		};
		// count = 2

		// console.log(digit + " === " + count);
		if (digit !== count) {
			isSelfDescribing = false;
		}
	};

	if (isSelfDescribing) {
		return "1";
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