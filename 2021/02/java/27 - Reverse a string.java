//reverse a string using for loop and array of chars
import java.util.*;

public class Test {

	public static void main(String[] args) {

		String str;
		Scanner sc = new Scanner(System.in);
		str = sc.next();

		int len = str.length();
		char[] tempCharArray = new char[len];
		char[] charArray     = new char[len];

		//put original string in an array of chars
		str.getChars(0, len, tempCharArray, 0);

		//reverse array of chars
		for (int i = 0; i < len; i++) {
			charArray[i] = tempCharArray[len - 1 - i];
		}

		String reverseStr = new String(charArray);

		System.out.println("Original: " + str);
		System.out.println("Reverse:  " + reverseStr);
		
	}
}