(function(){
	var startingRow = [1,2,3,4,5,6,7,8,9,10,11,12];
	var currentRowNumber = 1;
	var maxRow = 12;
	for (; currentRowNumber <= maxRow; currentRowNumber++) {
		var currentRow = [];
		for (var i = 0, len = startingRow.length; i < len; i++) {
			var digit = startingRow[i] * currentRowNumber;
			var digits = [digit.toString()];
			var padding = 3 - digit.toString().length;
			for (var num = 0; num < padding; num++){
				digits.push(" ");
			}
			currentRow.push( digits.reverse().join("") );
		}
		console.log( currentRow.join(" ") );
	};

}())