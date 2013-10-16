var RomanMapping = {
	"1" : "I",
	"2" : "II",
	"3" : "III",
	"4" : "IV",
	"5" : "V",
	"6" : "VI",
	"7" : "VII",
	"8" : "VIII",
	"9" : "IX",
	"10" : "X",
	"50" : "L",
	"100" : "C",
	"500" : "D", 
	"1000" : "M"
};

var processLine = function(line){
	var characters = line.split("").reverse();
	var digits = [];
	var romans = [];
	characters.forEach(function(character, index){
		digits[index] = parseInt(character, 10) * Math.pow(10, index);
	});
	console.log(digits);
	digits.forEach(function(digit, index){
		digit = parseInt(digit.toString().charAt(0), 10);
		if (digit !== 0){
			if (index === 0) {
				// 0's position number
				romans.push(RomanMapping[digit.toString()]);
			} else if (index === 1) {
				// 10's number
				if (digit === 4) {
					romans.push("XL");
				}
				else if (digit === 9){
					romans.push("XC");
				} else if (digit === 5) {
					romans.push("L");
				} else if (digit < 5 ) {
					for (var i = 0; i < digit; i++){
						romans.push("X");
					}
				} else if (digit > 5) {
					var loops = digit - 5;
					for (var i = 0; i < loops; i++) {
						romans.push("X");
					}
					romans.push("L");
				}
			} else if (index === 2) {
				// 100's position
				if (digit === 4) {
					romans.push("CD");
				} else if (digit === 9) {
					romans.push("CM");
				} else if (digit === 5) {
					romans.push("D");
				} else if (digit < 5) {
					for (var i = 0; i < digit; i++) {
						romans.push("C")
					}
				} else if (digit > 5) {
					var loops = digit - 5;
					for (var i = 0; i < loops; i++) {
						romans.push("C");
					}
					romans.push("D");
				}
			}
			else if (index === 3) {
				// 1000's position
				for (var i = 0; i < digit; i++) {
					romans.push("M"); // that many thousands.
				}
			}
		}
		

	});
	return romans.reverse().join("");
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var result = processLine(line);
  	console.log(result);
  }
});