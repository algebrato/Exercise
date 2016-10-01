import java.io.*;

public class Rot13{
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		for(;;) {
			System.out.print("> ");
			String line = in.readLine();
			if( (line.equals("")) || line.equals("quit") ){
				System.out.print("Stop\n");
				break;
			}
			StringBuffer buf = new StringBuffer(line);
			for(int i = 0; i < buf.length(); i++)
				buf.setCharAt(i,rot13(buf.charAt(i)));
			System.out.print(buf);
		}
	}

	public static char rot13(char c){
		if((c >= 'A') &&  ( c <= 'Z')){
			c+=13;
			if (c > 'Z')
				c -=26;
		}
		if((c >= 'a') &&  ( c <= 'z')){
			c+=13;
			if (c > 'z')
				c-=26;
		}
		return c;
	}
}
