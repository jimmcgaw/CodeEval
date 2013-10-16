var processLine = function(line){
	var json = JSON.parse(line);
	var items = json.menu.items;
	var sum = 0;
	for (var i = 0, len = items.length; i < len; i++) {
		var item = items[i];
		if (item && item.label) {
			sum += item.id;
		}
	}
	return sum;
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var result = processLine(line);
  	console.log(result);
  }
});