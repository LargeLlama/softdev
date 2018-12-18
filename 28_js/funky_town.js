var fibonacci = function(n)
{
	if (n < 2)
		return n;
	else
		return fibonacci(n - 1) + fibonacci(n - 2);
}

var gcd = function(a, b)
{
	if (b != 0)
		return gcd(b, a % b);
	else
		return a;
}

var generateList = function(length)
{
	var list = []
	for (i = 0; i < length; i++)
	{
		list.push("Student " + i);
	}
	return list;
}

var happy_feet = generateList(15);

var randomStudent = function()
{
	var index = Math.floor(Math.random() * happy_feet.length);
	return happy_feet[index];
}
