import java.util.*;

//: Classe principale
public class Main {
	public static void main(String[] args){
		/**Creato l'oggetto f di tipo foo*/
		foo f = new foo();
		System.out.println("Intero: "+f.a);
		System.out.println("Char:   "+f.b);
	}
} ///:

class foo{
	int a;
	char b;
}