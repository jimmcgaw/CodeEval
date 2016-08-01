var Rectangle = function(topLeftX, topLeftY, bottomRightX, bottomRightY){
  this.x = parseInt(topLeftX, 10);
  this.y = parseInt(topLeftY, 10);
  this.width = Math.abs(parseInt(bottomRightX, 10) - parseInt(topLeftX, 10));
  this.height = Math.abs(parseInt(topLeftY, 10) - parseInt(bottomRightY, 10));
};

Rectangle.prototype.hasCollision = function (otherRectangle) {
  if (this.x < otherRectangle.x + otherRectangle.width && this.x + this.width > otherRectangle.x && this.y < otherRectangle.y + otherRectangle.height &&this.height + this.y > otherRectangle.y) {
    return true;
  }
  return false;
};

var processLine = function(line){
	line = line.toLowerCase();
  var numbers = line.split(',');
  var rectA = new Rectangle(numbers[0], numbers[1], numbers[2], numbers[3]);
  var rectB = new Rectangle(numbers[4], numbers[5], numbers[6], numbers[7]);
  return rectA.hasCollision(rectB) ? 'True' : 'False';
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line !== "") {
  	var result = processLine(line);
  	console.log(result);
  }
});
