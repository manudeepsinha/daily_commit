/*automatic conversion of primitive data types to the object of its corresponding wrapper class is called autoboxing.
  eg: int to Integer, long to Long, boolean to Boolean

  automatic converting object of wrapper class to its corresponding primitive data type is called unboxing.
  eg: Integer to int, Long to long, Boolean to boolean
*/
public class autoboxing {
	public static void main(String [] args){

		int i = 10;

		//autoboxing -> primitive to Integer object conversion
		Integer I = i;

		//unboxing -> Integer object to primitive data type conversion
		int j = I;

		ArrayList<Integer> arrayList = new ArrayList<Integer>();

		//autoboxing -> ArrayList only stores objects
		arrayList.add(25);

		//unboxing -> method returns an Integer object
		int num = arrayList.get(0);

		//printing the value from object
		System.out.println(arrayList.get(0));

		//printing the value from variable
		System.out.println(num);	
	}
}