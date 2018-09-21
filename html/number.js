console.log("fjsf");
function hello() {
	const number = parseInt(document.getElementById("Num").value);
	var body = document.getElementByTagName('body')[0];
	var tb1 = document.createElement('table');
	tb1.style.width = '100%';
	tb1.setAttribute('border', '1');
	var tbdy = document.createElement('tbody');
	for (let 1=1, i<11; i++){
		var tr = document.createElement('tr');
		var td = document.createElement('td');
		var data = document.createTextNode(`${number}*${i} = ${number * i}`);
		td.appendChild(data);
		tr.appendChild(td);
		tb1.appendChild(tr);
	}
	body.appendChild(tb1)
}