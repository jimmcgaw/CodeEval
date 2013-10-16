// given a number x, get array of all factors
// for x (except for 1 and x)
var getFactors = function(x){
	var factors = [];
	var i = Math.ceil(x/2);
	for (; i >= 2; i--) {
		if (x % i == 0){
			factors.push(i);
		}
	};
	return factors;
};

var Customer = function(name) {
	this.name = name;
};

Customer.prototype.getLetters = function(){
	return this.name.match(/[a-zA-z]/g);
};

Customer.prototype.getVowels = function(){
	return this.getLetters().join("").match(/[aeiouy]/g);
};

Customer.prototype.getConsonants = function(){
	return this.getLetters().join("").match(/[^aeiouy]/g);
};

var Product = function(name) {
	this.name = name;
};

Product.prototype.getLetters = function(){
	return this.name.match(/[a-zA-z]/g);
};

Product.prototype.getVowels = function(){
	return this.getLetters().join("").match(/[aeiouy]/g);
};

Product.prototype.getConsonants = function(){
	return this.getLetters().join("").match(/[^aeiouy]/g);
};

// will return true if letter count is even, false if odd
Product.prototype.letterCountEven = function(){
	return this.getLetters().length % 2 == 0;
};

Product.prototype.computeScore = function(customer) {
	var score = 0;
	if (this.letterCountEven()) {
		score = customer.getVowels().length * 1.5;
	} else {
		score = customer.getConsonants().length;
	}

	var productFactors = getFactors( this.getLetters().length );
	var customerFactors = getFactors( customer.getLetters().length );

	var hasCommonFactors = false;
	productFactors.forEach(function(productFactor){
		customerFactors.forEach(function(customerFactor){
			if (productFactor === customerFactor){
				hasCommonFactors = true;
			}
		});
	});

	if (hasCommonFactors){
		score = score * 1.5;
	}

	return score;
};

var Milo = function(raw_data){
	// scores for each customer by product
	this.productScores = {};
	// scores for each product by customer
	this.customerScores = {};

	var customerNames = raw_data.split(";")[0].split(",");
	var productNames = raw_data.split(";")[1].split(",");
	this.customers = customerNames.map(function(name){ return new Customer(name); });
	this.products = productNames.map(function(name){ return new Product(name); });

	this.computeScores();
};

Milo.prototype.computeScores = function(){
	var scores = [];
	var self = this;
	this.products.forEach(function(product){
		var customerScoresForProduct = {};
		self.customers.forEach(function(customer){
			var score = product.computeScore(customer);
			customerScoresForProduct[customer.name] = score;
			scores.push(product.computeScore(customer));
		});
		self.productScores[product.name] = customerScoresForProduct;
	});
};

Milo.prototype.getScores = function(){
	return this.productScores;
};

var fs  = require("fs");
var sum = fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
  if (line != "") {
  	var milo = new Milo(line);
  	var result = milo.getScores();
  	console.log(result);
  }
});