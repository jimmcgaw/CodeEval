var fs  = require("fs");

fs.stat(process.argv[2], function(err, stats){
	console.log(stats.size);
});

