class InvalidBalanceException extends Exception {

	public InvalidBalanceException(String message) {	//constructor
		super(message);
	}
}

public class ExceptionDemo {

	public static void main(String[] args) {

		int balance;
		try {
			balance = Integer.parseInt(args[0]);
			updateBalance(balance);
		}

		catch (InvalidBalanceException ex) {
			System.out.println("Caught in catch of InvalidBalanceException");

			ex.printStackTrace();
		}

		catch (NumberFormatException ex) {
			System.out.println("Caught in catch of NumberFormatException");
		}

		catch (ArrayIndexOutOfBoundsException ex) {
			System.out.println("Caught in catch of ArrayIndexOutOfBoundsException");
		}

		catch (Exception ex) {
			System.out.println("Encountered with new type of exception.");
		}

		System.out.println("main() method runs successfully");
	}

	public static int updateBalance(int number) throws InvalidBalanceException {

		if (number < 0)
			throw (new InvalidBalanceException("Account balance cannot be less than zero!"));

		System.out.println("No exception occurred in updateBalance() method.");
	}
}