var isPrime = function(number) {
	var is_prime = true;
	var divisor = Math.ceil(number / 2);
	while (divisor > 1){
		if (number % divisor === 0) {
			is_prime = false;
			break;
		}
		divisor--;
	}
	return is_prime;
};

var primeSum = 0;
var myNumber = 2;
var primeCount = 0;
while(primeCount < 1000){
	var prime = isPrime(myNumber);
	if (prime){
		primeSum += myNumber;
		primeCount++;
	}
	myNumber++;
}

console.log(primeSum);