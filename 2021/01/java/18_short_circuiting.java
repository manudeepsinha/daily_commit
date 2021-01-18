public class test{

	public static void main(String [] args){

		Scanner sc = new Scanner(System.in);
		String user = "Manudeep" , pwd = "HeyWorld";
		String iu = sc.next();
		String ip = sc.next();

		/*short circuiting is done, i.e. with logical and op., if first cond. is false, doesn't check second cond. 
		{similar approach in logical or} */
		if(user.equals(iu) && pwd.equals(ip))
			System.out.println("Hello, user!");
		else
			System.out.println("Wrong password!");

	}
}