//check palindrome 
import java.util.*;

class Main {

	public static int checkPalindrome(String str) {

		int len = str.length();
		int count = 0;
		char [] aString = new char[len];

		str.getChars(0,len, aString, 0);

		for (int i = 0; i < len / 2; i++) {

			if (aString[i] == aString[len - 1 - i])
				count ++;
		}
		if (count == len / 2)
			return 1;
		else
			return 0;

	}
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		String str;
		System.out.println("Enter a string to check palindrome: ");
		str = sc.next();

        if (checkPalindrome(str) == 1)
			System.out.println("palindrome");
		else
			System.out.println("not palindrome");
		
		
	}
}