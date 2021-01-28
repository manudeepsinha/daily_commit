public class ExceptionDemo {

	public static void main (String[] args) {
		try {
			methodA();

			System.out.println("Exit try of main()");
		}

		catch (ArithmeticException ex) {

			System.out.println("Exception caught!");

			ex.printStackTrace();
		}

		finally {

			System.out.println("Executed main()");
		}

		System.out.println("Exit main()");

	}

	public static void methodA() throws ArithmeticException {

		int a = 5, c;
		System.out.println("Enter the value of variable b: ");
		Scanner in = new Scanner(System.in);

		b = in.nextInt();

		if (b == 0)
			throw new ArithmeticException();
		else
			c = a/b;

		System.out.println("Exit methodA()");
	}

}