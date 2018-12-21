//global/constantly used variables so they are defined at the top
var list = document.getElementById('thelist');
var fiblist = document.getElementById('fiblist');
var fibNum = 0;

//our fibonacci function, from K28
var fibonacci = function(n)
{
	if (n < 2)
		return n;
	else
		return fibonacci(n - 1) + fibonacci(n - 2);
}

//func to add items to the regular list
var addItem = function()
{
	var entry = document.createElement('li');
	entry.innerHTML = 'UwU'; //there is ONLY UwU
	list.appendChild(entry);
}

//func to add items to the fiblist
var addFib = function()
{
	var entry = document.createElement('li');
	//console.log(fibonacci(fibNum)); debug
	entry.innerHTML = fibonacci(fibNum);
	fiblist.appendChild(entry);
	fibNum += 1;

}

//get the button w/ id = b, and make it so when it's clicked our addItem function is called
document.getElementById('b').addEventListener('click', addItem);

//when the item is clicked, remove it
list.addEventListener('click', function(e)
	{
		e.target.remove();
	});

//when the mouse is over a list element, change the heading to the contents of the list element
list.addEventListener('mouseover', function(e)
	{
		document.getElementById('h').innerHTML = e.target.innerHTML;
	});

//when the mouse is moved off the item, set the heading back to Hello World
list.addEventListener('mouseout', function(e)
	{
		document.getElementById('h').innerHTML = "Hello World";
	});

//when the button with id = "fb" is clicked, add to the fib list :3
document.getElementById('fb').addEventListener('click', addFib); 
