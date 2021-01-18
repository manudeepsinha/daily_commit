/*faster compared to scanner as buffer reader does not do post processing of the data and simply reads the character stream.
it has larger buffer to read data than scanner.
flexible as buffer size can be defined to read each time.
synchronized and preferred when using multiple threads.
*/
import java.io.* ;

public class test{
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter a string: ");
		String s = br.readLine();
		System.out.println("You've entered: " + s);

		BufferedReader br_int = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter an integer: ");
		int i = Integer.parseInt(br_int.readLine());
		System.out.println("You've entered: " + i);

	}
}