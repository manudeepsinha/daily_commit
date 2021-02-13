import java.util*

public class Test {
    public static void main(String[] args) {

        String s1 = "Hello";                //literal
        String s2 = "Hello";                //made only one Hello in common pool and s1,s2,s3 pointing to same literal
        String s3 = s1;
        String s4 = new String("Hello");    //object
        String s5 = new String("Hello");    //stack stores s4,s5 that points to two different "Hello" that're stored in heap 

        if (s1 == s2) {
            System.out.println("String s1 equals to s2");
        }

        if (s5.equals(s4)) {           //s4 == s5 will match location in heap and not contents of object
            System.out.println("Right way to compare strings");
        }

        System.out.println(s4.length());
        System.out.println(s5.toUpperCase());
    }
}