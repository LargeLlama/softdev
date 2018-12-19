//recursive implementation of fibonacci sequence
var fibonacci = function(n)
{
	if (n < 2)
		return n;
	else
		return fibonacci(n - 1) + fibonacci(n - 2);
}

//recursive implementation with gcd
//how it works: 
//give two numbers, a and b
//if b is not 0, then we run gcd again, but the parameters modified
//gcd(b , a % b) - b is now a, and the new value for b is the module of a and b
//this repeats until b finally reaches 0, at which point we would return a, the gcd
var gcd = function(a, b)
{
	if (b != 0)
		return gcd(b, a % b);
	else
		return a;
}

//generates a list of length length,
//the format as follows
//[ "Student 1", "Student 2", "Student 3", ... "Student length"]
//uses a for loop
var generateList = function(length)
{
	var list = [];

	for (i = 0; i < length; i++)
	{
		list.push("Student " + i); //adding to lists is supported by JS with the .push() function
	}

	return list;
}

//the hard coded list
var happy_feet = generateList(15);

//produces random student from the list
var randomStudent = function()
{
	//utiltizes the built-in Math library to procure a random number between 0 and the length of the list
	var index = Math.floor(Math.random() * happy_feet.length);
	return happy_feet[index];
}
