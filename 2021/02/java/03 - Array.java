import java.util.*

public class Test {

	public static void main(String[] args) {

		int numItems;
		int [] items;
		Scanner in = new Scanner(System.in);

		System.out.println("Enter the number of items: ");
		numItems = in.nextInt();

		items = new items[numItems];

		if (items.length > 0) {
			System.out.println("Enter the value of all the items, space seperated:");
			for(int i = 0; i < items.length; ++i)
				items[i] = in.nextInt();
		}

		System.out.print("The elements of the array are: [");
		
		for (int value : items) {
			if (value == items[0])
				System.out.print(value);
			else
				System.out.print(", " + value);
		}

		System.out.print("]");
		in.close();
	}
}