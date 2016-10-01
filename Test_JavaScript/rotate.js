var angle = 0;
var raggio = 117;
var speed =5;
var posL = 0;
var L = raggio * speed * Math.PI / 360;
var time = setInterval(roto_trasl,50);
var n_rot = 0;


function roto(){
	if (angle >= 360) {
		angle = 0;
		n_rot++;
	}
	angle+=speed;

	return angle;
}


function trasl(){
	posL += L;
	return posL;
}




function roto_trasl(){
	if(n_rot ==1){
		clearInterval(time);
	} else {
		document.getElementById("Rotate").style.position = "relative";
		document.getElementById("Rotate").style.left = trasl();
	}
	
	jQuery('#Rotate').rotate(roto());
	
}
