var myArray = [];

var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
    	var numbers = line.split(" ");
    	var i, len = numbers.length;
    	for (i = 0; i < len; i++){
    		myArray.push(numbers[i]);
    	}
    	var toPrint = [];
    	for (i = 0; i < len; i++){
    		var num = myArray.pop();
    		if (i % 2 == 0){
    			toPrint.push(num);
    		}
    	}
    	console.log(toPrint.join(" "));
    	myArray.length = 0;  // clear the array for next cycle
    }
});