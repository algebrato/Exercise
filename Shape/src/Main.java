import java.lang.System;
import java.util.ArrayList;
public class Main {
	public static void printa(int s){
		System.out.println(s);
	}
	
	public static void faicose(Shape s){
		s.draw();
		s.erase();
		printa(s.d);
		
	}

	public static void main(String[] args){
		Circle c = new Circle();
		Square sq = new Square();
		Shape ss = new Shape();
		/*faicose(c);
		faicose(sq);
		faicose(ss);*/
		ArrayList<Shape> shapes = new ArrayList<Shape>();
		shapes.add(0,c);
		shapes.add(1,sq);
		shapes.add(2,ss);
		for(int i=0; i<3; ++i)
			faicose(shapes.get(i));
		
		
	}
}

class Shape {
	public int d = 2;
	void erase(){
		System.out.println("Erase Shape");
	}
	void draw(){
		System.out.println("Draw Shape");
	}
	
}

class Square extends Shape{
	void erase(){
		System.out.println("Erase Square");
	}
	void draw(){
		System.out.println("Draw Square");
	}
}

class Circle extends Shape{
	void erase(){
		System.out.println("Erase Circle");
	}
	void draw(){
		System.out.println("Draw Circle");
	}
}


class Triangle extends Shape{
	void erase(){
		System.out.println("Erase Triangle");
	}
	void draw(){
		System.out.println("Draw Triangle");
	}
}