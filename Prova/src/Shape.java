//import java.util.ArrayList;

class Shape {
	public static void main(String[] args){
		Oggetto3D obj3d = new Oggetto3D();
		Oggetto2D obj2d = new Oggetto2D();
		Oggetto1D obj1d = new Oggetto1D();
		Punto pnt = new Punto();
		Class2 cl2 = new Class2();
		
		System.out.println("Oggetto 3d = "+obj3d.d);
		System.out.println("Oggetto 2d = "+obj2d.d);
		System.out.println("Oggetto 1d = "+obj1d.d);
		System.out.println("Oggetto 0d = "+pnt.d);
	}
}


abstract class Oggetto {
	public int d = 0;
}

class  Oggetto3D extends Oggetto {
	Oggetto3D(){
		System.out.println("Costruito Oggetto3D");
		d = 3; 
		}

}

class Oggetto2D extends Oggetto {
	Oggetto2D(){ d = 2; }
}

class Oggetto1D extends Oggetto {
	Oggetto1D(){ d = 1; }
}

class Punto extends Oggetto {
	Punto(){ d = 0; }
}

