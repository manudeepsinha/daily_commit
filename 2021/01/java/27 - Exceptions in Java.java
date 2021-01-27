import java.util.Scanner ;

public class test{
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		int b = sc.nextInt();
		myMethodA(b);
		myMethodB(b);
	}

	public void myMethodA(int b) throws ArithmeticException {
		int a,b,c;
		this.b = b;
		//user input b
		if (b == 0)
			throw new ArithmeticException();
		c = a/b;


		System.out.println(c);
	}

	public void myMethodB(int b) {
		int a,b,c;
		this.b = b;
		try{
			//user input for b
			c = b/a;

		}
		catch (ArithmeticException ex){

			System.out.println("Exception caught!")
		}
	}
}