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

var isPalendrome = function(number){
	var num_string = number.toString();
	return num_string === num_string.split("").reverse().join("");
}

var myNumber = 1000;
while(myNumber > 0){
	var prime = isPrime(myNumber);
	var palendrome = isPalendrome(myNumber);
	if (prime && palendrome){
		console.log(myNumber);
		break;
	}
	myNumber--;
}