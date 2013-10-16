var fs  = require("fs");

var QueryBoard = function(){
	this.edgeLength = 256;
	this.rows = [];
	var initialRow = [];
	var i = 0;
	do {
		initialRow.push(0);
		i++;
	} while (i<this.edgeLength);

	i = 0;
	do {
		this.rows.push(initialRow.slice()); // 'slice' does deep copy of array
		i++
	} while (i<this.edgeLength);

};

QueryBoard.prototype.getBoard = function(){
	return this.rows;
};

QueryBoard.prototype.executeAction = function(command){
	var items = command.split(" ");

	var action = items[0];
	var updateIndex = parseInt(items[1], 10) - 1;
	var value = parseInt(items[2], 10);

	if (action === "SetCol") {
		for (var i = 0, len = this.rows.length; i < len; i++) {
			var row = this.rows[i];
			row[updateIndex] = value;
		}
	}	else {
		// "SetRow"
		var row = this.rows[updateIndex];
		for (var i =  0, len = row.length; i < len; i++) {
			row[i] = value;
		}
	}
	return "";
};

QueryBoard.prototype.runQuery = function(command){
	var items = command.split(" ");
	var query = items[0];
	var queryIndex = parseInt(items[1], 10) - 1;
	var sum = 0;
	if (query === "QueryCol") {
		for (var i = 0, len = this.rows.length; i < len; i++) {
			var row = this.rows[i];
			sum += row[queryIndex];
		}
	} else {
		// "QueryRow"
		var row = this.rows[queryIndex];
		for (var i =  0, len = row.length; i < len; i++) {
			sum += row[i];
		}
	}
	return sum;
};

QueryBoard.prototype.processCommand = function(command){
	var items = command.split(" ");
	if (items.length === 2) {
		return this.runQuery(command);
	} else if (items.length === 3) {
		return this.executeAction(command);
	}
};

var qb = new QueryBoard();

var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
		var result = qb.processCommand(line);
		if (result !== ""){
			console.log(result);
		}
  }
});