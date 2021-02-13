//pending regexe(12:46) on video 37 Java(GFG Placement 100)
import java.util*

public class Test {
    public static void main(String[] args) {

        String s1 = "hey Hello Hello World";                
        String s2 = "Hello";                
        String s3 = s1;
        String s4 = new String("HeLlO");    
        String s5 = new String("World");

        //length
        System.out.println(s4.length());    //5
        System.out.println(s4.isEmpty());   //false

        //comparison
        if (s1 == s2) {                 //not the way to compare two strings
            System.out.println("String s1 equals to s2");
        }

        if (s1.equals(s4))             //s4 == s5 will match location in heap and not contents of object
            System.out.println("Right way to compare strings");

        else if (s2.equalsIgnoreCase(s4))
            System.out.println("How can s5 be equals to s4?");  //runs this block
        
        else
            System.out.println("Didn't match any.");

        System.out.println(s1.compareTo(s4));           // 32 //return 0 if same. <0 if lexicographically less than another; else >0
        System.out.println(s1.compareToIgnoreCase(s4)); //13
        /*
        boolean startsWith(string another)

        //search begins at fromIndex
        boolean startsWith(String another, int fromIndex)
        boolean endsWith(String another)
        */

        //searching and indexing
        System.out.println(s1.indexOf(s2));         //4
        System.out.println(s1.indexOf(s2,2));       //4
        System.out.println(s1.indexOf('L'));        //-1
        System.out.println(s1.indexOf('L',3));      //-1

        System.out.println(s1.lastIndexOf(s2));     //10
        System.out.println(s1.lastIndexOf(s2,3));   //-1
        System.out.println(s1.lastIndexOf('o'));    //17
        System.out.println(s1.lastIndexOf('o',5));  //-1

        System.out.println(s1.charAt(2));           //y
        System.out.println(s1.substring(5));        //ello Hello World
        System.out.println(s1.substring(5,10));     //ello     //10 is exclusive

        //modify
        System.out.println(s1.toUpperCase());       //HEY HELLO HELLO WORLD
        System.out.println(s1.toLowerCase());       //hey hello hello world
        System.out.println(s1.trim());              //hey Hello Hello World              //removes whitespaces from front and back

        System.out.println(s1.replace('H','M'));    //hey Mello Mello World
        System.out.println(s1.concat(s2));          //hey Hello Hello WorldHello
        System.out.println(s1.toCharArray());       //hey Hello Hello World       //used in CP

        /*copy into destination char[]
        void sourceString.getChars(int sourceBegin, int sourceEnd, char[] destination, int destinationBegin);
        */
    }
}