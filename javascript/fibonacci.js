var SequenceGenerator = function(){
	this.sequence = [0, 1];
};

SequenceGenerator.prototype.getDigit = function(index){
	if (this.sequence.length < index+1) {
		// generate the additional values
		while (this.sequence.length < index+1) {
			this.generate();
		}
 	}
	return this.sequence[index];
};

SequenceGenerator.prototype.generate = function(){
	var lastIndex = this.sequence.length-1;
	var penultimateIndex = this.sequence.length-2;
	this.sequence.push(this.sequence[penultimateIndex] + this.sequence[lastIndex]);
};

var processLine = function(line){
	var sg = new SequenceGenerator();
	var index = parseInt(line, 10);
	return sg.getDigit(index);
};

var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line != "") {
    	var result = processLine(line);
    	console.log(result);
    }
});