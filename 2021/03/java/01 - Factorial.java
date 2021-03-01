//program for strong numbers
import java.util.*;

public class Main {

	public static int factorial(int num) {

		if (num == 1)
			return 1;

		else
			return num * factorial(num - 1);
	}

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		System.out.println("Enter a number more than 1: ");
		int number = sc.nextInt();
		if (number > 1) {

			System.out.println("The factorial is: " + factorial(number));
		}
		else
			System.out.println("Invalid input!");

	}
}