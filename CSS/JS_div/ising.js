var size=150;  
var IsingModel =new terra.Terrarium(
		size,size,
		"IsingModel",
		0.75,
		document.getElementById('placeholder'),
		true,
		'vonNeumann',
		0,
		'transparent'
		);
  
var magnetization = 0;
var counter=0;
terra.registerCA({  
  type: 'Ising',    
  colorFn: function ()  
  {
	return this.state==1 ? '255,255,255,255' : '0,0,0,255';
  },
  process: function (neighbors) 
  {
	counter+=1;
	if (counter==size*size)
	{ 
		document.getElementById("printM").innerHTML = magnetization.toFixed(3);
		document.getElementById("printT").innerHTML = temp.toFixed(3);
		counter=magnetization=0;
	} 
	magnetization +=this.state/(size*size);
	temp =	parseFloat(document.getElementById("T").value);
	document.getElementById("printT").innerHTML = temp;
	deltaE = 0;
	for (var i = 0; i < neighbors.length; i++){ 
		deltaE += neighbors[i].creature.state;
	}
	if (neighbors.length<8)
		deltaE *= 8/neighbors.length;
	deltaE *= this.state;  
	if (deltaE<0)          
		this.state *= -1;  
	else if (Math.random() < Math.min(1.0,Math.exp(-deltaE*0.5/temp)) )
	{ 
		this.state *= -1; 
	}
  }
},function (){
	this.alive=true;
	if(Math.random() < 0.5 ){
		this.state = 1;
	}else{
		this.state = -1;
	}
});
IsingModel.grid = IsingModel.makeGrid('Ising');
IsingModel.animate();
