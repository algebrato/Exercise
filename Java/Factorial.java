public class Factorial{
	public static long factorial(long x){
			if (x <= 1) return 1;
			else return x * factorial(x-1);
	}
}
