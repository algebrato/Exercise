import java.io.*;

public class RectTest{
	public static void main(String[] args){
		Rect r1 = new Rect(1,1,4,4);
		Rect r2 = new Rect(2,3,5,6);
		Rect i = r2.intersection(r1);
		
		DrawableRect rd = new DrawableRect(5,7,10,7);

		System.out.println(i);
	}
}	
