

class Shape {

	protected void wim(){
		System.out.println("Funzione WIM di SHAPE");
	}
	
	public static void main(String args[]){
		Shape sh = new Square();
		sh.wim();
	}
}

class Square extends Shape {
	protected void wim(){
		System.out.println("Funzione WIM di Square");
	}
}



