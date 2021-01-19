//small demonstration for if-else statement
import java.util.Scanner;	
	public class test{
		public static void main(String [] args){
			Scanner sc = new Scanner(System.in);
			System.out.println("Please enter a number: ");
			int num = sc.nextInt();
			checkEven(num);
		}

		public static void checkEven(int num){
			if(num%2 == 0)
				System.out.println("It's an even number.");
			else
				System.out.println("It's an odd number.");
		}
	}