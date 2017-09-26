/* 
def fb():
	lista = []
	for i in range(1, 18):
		if i % 3 == 0:
			lista.append("Fizz")
		elif i % 5 == 0:
			lista.append("Buzz")
		elif i % 3 == 0 and i % 5 == 0:
			lista.append("FizzBuzz")
		else:
			lista.append(i)
	return lista
*/


var fb = function() {
  var a = [];
  /* seu codigo aqui */
  for(var i = 1; i < 18; i++){
  
  if(i % 3 === 0 && i % 5 === 0){
  	a.push("FizzBuzz")
  }
  else if(i % 5 === 0){
  	a.push("Buzz")
  }
  else if(i % 3 === 0){
  	a.push("Fizz")
   }
  else{
  	a.push(i)
  }
  }
  return a;

}
console.log(fb());
