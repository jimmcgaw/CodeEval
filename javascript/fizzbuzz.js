/*Sample code to read in test cases:*/
var fs  = require("fs");
fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== "") {
        var elements = line.split(" ");
        var a = elements[0];
        var b = elements[1];
        var upper_bound = elements[2];
        var seq = [];
        var i;
        for (i = 1; i <= upper_bound; i++) {
            var value = i;
            if ( i % a === 0) {
                value = "F";
            }
            if ( i % b === 0) {
                value = "B";
            }
            if ( i % a === 0 && i % b === 0) {
                value = "FB";
            }
            seq.push(value);
        }
        console.log(seq.join(" "));
        //do something here
        //console.log(answer_line);
    }
});