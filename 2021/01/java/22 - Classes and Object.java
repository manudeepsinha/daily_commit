//basic implementation of OOP using 2 classes interacting with each other
public class Complex {
	int real, imag;
	void print(){
		System.out.println(real + " +i" + imag);
	}

	complex(int r, int i) {		//constructor of the class complex
		real = r;
		imag = i;
	}

	void add( Complex c) {

		real = real + c.real;
		imag = imag + c.imag;	
	}
}

public class test {
	public static void main(){
		Complex c1 = new Complex(10,20);
		c1.print();
		Complex c2 = new Complex(20,30);
		c1.add(c2);
		c1.print();

	}

}
