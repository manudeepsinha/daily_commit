class Point {

	int x; //default initialized as 0 as it's in non-primitive data type
	int y;
}

public class first {
    
    public static void main(String [] args)
    {
        Point p1 = new Point(); //allocates memory in the heap
        p1.x = 10;
        p1.y = 20;

        Point p2 = p1; //doesn't allocate memory in the heap. only make reference to the p1
        p2.x = 30;

        //pointing to the values (reference) is done for non-primitive data types
        System.out.println(p1.x);
        System.out.println(p2.x);

        int a = 10;
        int b = a; //memory allocated in the stack
        b = 30;

        //new value is assigned for primitive data types
        System.out.println(a);
        System.out.println(b);
    }
}