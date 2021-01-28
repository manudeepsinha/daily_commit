import java.io.File;
import java.io.FileNotFoundException;

public class ExceptionDemo {

	public static void main (String[] args) {
		try {
			methodA();

			Scanner in = new Scanner(new File("test.in"));

			System.out.println("Exit try of main()");
		}

		catch (ArithmeticException ex) {

			System.out.println("ArithmeticException caught!");

			ex.printStackTrace();
		}

		catch (FileNotFoundException ex) {

			System.out.println("FileNotFoundException caught!");
		}

		catch (Exception ex) {

			System.out.println("New exception has occurred");
		}

		finally {

			System.out.println("finally in main()");
		}

		System.out.println("Exit main()");

	}

	public static void methodA() throws ArithmeticException {

		System.out.println("Enter methodA()");

		try {

			System.out.println(1/0);
		}

		finally {
			System.out.println("finally in methodA()");
		}

		System.out.println("Exit methodA()");
	}

}