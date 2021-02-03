/*Java code for Linear Search
*/
import java.util.*

public class Test {

	//Linear Search
	public static int linearSearch(int arr[], int x) {

		for (int i = 0; i < arr.length; i++){
			if (arr[i] == x) {
				return i;
			}
		return -1;
		}

	}

	//main method
	public static void main(String[] args) {

		int num;
		int index;
		int arr[] = {10, 4, 21, 1, 46, 35, 11, 13, 123};
		Scanner in = new Scanner(System.in);

		System.out.println("Enter the value to find in the array: ");
		num = in.nextInt();

		index = linearSearch(arr,num);
		if (index == -1)
			System.out.println("The value doesn't exist in the array.");
		else
			System.out.println("The value exist on " + index + " index.");
	}

}