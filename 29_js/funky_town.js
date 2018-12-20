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

//functions to call upon button press - just sets values based off the methods in here
var genFib = function()
{
	var fib = document.getElementById("fib");
	var num = document.getElementById("input");
	num.innerHTML = "Running fibonacci(" + document.getElementById("num").value + ")";
	fib.innerHTML = fibonacci((document.getElementById("num").value));
}

var genStudent = function()
{
	var student = document.getElementById("student");
	student.innerHTML = " The random student is " + randomStudent();
}

var genGCD = function()
{
	var a = document.getElementById("a").value;
	var b = document.getElementById("b").value;
	console.log(a);
	console.log(b);
	console.log(gcd(a, b));
	var ans = document.getElementById("gcd_ans");
	ans.innerHTML = "GCD of " + a + " and " + b + " is <strong>" + gcd(a, b) + "</strong>";
}
