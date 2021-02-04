/*
Following is the code for practice problem: https://www.hackerrank.com/challenges/java-static-initializer-block/problem?isFullScreen=true
*/
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

//Write your code here
static Scanner in = new Scanner(System.in);
static int B = in.nextInt();
static int H = in.nextInt();
static boolean flag = true;
static{ 
    if (B < -100 || H < -100 || B > 100 || H > 100)
            flag = false;
    try{
        
        if (B <= 0 || H <= 0){
            flag = false;
            throw new Exception ("Breadth and height must be positive");
        }
    }
    catch (Exception e){
        System.out.println(e);
    }
}//end of static

public static void main(String[] args){
		if(flag){
			int area=B*H;
			System.out.print(area);
		}
		
	}//end of main

}//end of class