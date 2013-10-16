/*Sample code to read in test cases:*/

var compareBitPostions = function(number, bit_index1, bit_index2) {
	var binNumber = parseInt(number,10).toString(2);
	var bits = binNumber.split("");
	bit_index1--;
	bit_index2--;
	if (bit_index1 > bits.length || bit_index2 > bits.length) {
		return "false";
	}
	// console.log(bits);
	// console.log(bit_index1);
	// console.log(bit_index2);

	return (bits[bit_index1] === bits[bit_index2]).toString();
};

var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
    		var elements = line.split(",");
    		console.log(compareBitPostions(elements[0], elements[1], elements[2]));	
    	
    }
});