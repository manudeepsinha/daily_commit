//small demostration for methods and non-primitive calling (reference) {some problem executing the code}
import java.util.Scanner;

	public class Point{
		int x,y;
	}

	public class test{
		public static void main(String [] args){
			Point p = new Point();
			p.x = 10;	 p.y = 20;
			fun(p);
			System.out.println(p.x + " " + p.y);	//value gets changed
			funs(p);
			System.out.println(p.x + " " + p.y);	//value unchanged
		}

		public static void fun(Point p){
			p.x = 20;
			p.y = 20;
		}

		public static void funs(Point p){
			Point p = new Point();						//new Point p is made and pointing to another set of x and y
			p.x = 0;
			p.y = 0;
		}
	}