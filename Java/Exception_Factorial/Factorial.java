import java.math.BigInteger;
import java.util.*;

public class Factorial{
		protected static Vector table = new Vector();

		//Inizializzato il primo elemento
		static {
				table.addElement(BigInteger.valueOf(1));
		}

		public static synchronized BigInteger factorial(int x){
				if(x < 0) throw new IllegalArgumentException("x non deve essere negativo");
				for(int size = table.size(); size <= x; size++){
						BigInteger lastfact = (BigInteger)table.elementAt(size-1);
						BigInteger nextfact = lastfact.multiply(BigInteger.valueOf(size));
						table.addElement(nextfact);
				}
				return (BigInteger) table.elementAt(x);
		}

		public static void main(String[] args){
				for(int i = 1; i<=50; i++)
						System.out.println(i + "! = " + factorial(i));
		}
}
