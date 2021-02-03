/*Java code for Binary Search
*/
import java.util.*

public class Test {

	//Binary Search
	public static int binarySearch(int arr[], int left, int right, int x) {

		if (left <= right) {

			int mid = (left + right) / 2;

			if (arr[mid] == x)
				return mid;

			if (arr[mid] < x)
				return binarySearch(arr, mid + 1, right, x);

			return binarySearch(arr, left, mid - 1, x);
		}
		
		return -1;
	}

	//main method
	public static void main(String[] args) {

		int num;
		int index;
		int arr[] = {2, 23, 32, 35, 46, 58, 61, 67, 89, 123, 145, 156, 199, 250};
		Scanner in = new Scanner(System.in);

		System.out.println("Enter the value to find in the array: ");
		num = in.nextInt();

		index = binarySearch(arr, 0, arr.length - 1, num);
		if (index == -1)
			System.out.println("The value doesn't exist in the array.");
		else
			System.out.println("The value exist on " + index + " index.");
	}

}