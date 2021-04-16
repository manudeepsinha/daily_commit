import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static void main(String args[] ) throws Exception {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    ToastMasters[] t = new ToastMasters[5];        
        Scanner sc = new Scanner(System.in);
        
        for(int i = 0;i<t.length;i++)
        {
            int id = sc.nextInt();sc.nextLine();
            String location = sc.nextLine();
            String type = sc.nextLine();
            int NoOfEvents = sc.nextInt();
            int NoOfYears =  sc.nextInt();
            t[i] = new ToastMasters(id,location,type,NoOfEvents,NoOfYears);
        }
        sc.nextLine();
        String loc = sc.nextLine();
        System.out.println("Total Count of "+loc+" : "+specificLocationCount(t,loc));
        ToastMasters t1[] = updateType(t);    
        for(int i=0;i<t1.length;i++)
            System.out.println(t1[i].getId()+"  "+t1[i].getLocation()+"  "+t1[i].getType());
    }
    
    public static int specificLocationCount(ToastMasters[] t,String loc)
    {
        //implement the method
        int count = 0;
        for (ToastMasters T : t) {
            if (T.getLocation().equalsIgnoreCase(loc)) {
                if (T.getNoOfEvents() > 10)
                    count++;
            }
        }
        return count;
    }
    
    public static ToastMasters[] updateType(ToastMasters[] t)
    {
        //implement the method
        int count = 0; 
        int index = 0;
        for (ToastMasters T : t) {
            if (T.getType().equals("Member") && T.getNoOfEvents() > 8){
                if (T.getNoOfYears() > 3) {
                    count++;
                }
            }
        }
        ToastMasters[] newT = new ToastMasters[count];
        for (ToastMasters T : t) {
            if (T.getType().equals("Member") && T.getNoOfEvents() > 8){
                if (T.getNoOfYears() > 3) {
                    T.setType("Host");
                    int id = T.getId();
                    String location = T.getLocation();
                    String type = T.getType();
                    int NoOfYears = T.getNoOfYears();
                    int NoOfEvents = T.getNoOfEvents();
                    newT[index] = new ToastMasters(id, location, type, NoOfEvents, NoOfYears);
                    index++;
                }
            }
        }
        return newT;
    }
    
}

class ToastMasters
{
    //implement the class
    private int id;
    private String location;
    private String type;
    private int NoOfEvents;
    private int NoOfYears;
    
    public int getId() {
        return id;
    }
    public String getLocation() {
        return location;
    }
    public String getType() {
        return type;
    }
    public int getNoOfEvents() {
        return NoOfEvents;
    }
    public int getNoOfYears() {
        return NoOfYears;
    }
    public void setType(String newType) {
        this.type = newType;
        return;
    }
    
    ToastMasters(int id, String location, String type, int NoOfEvents, int NoOfYears) {
        this.id = id;
        this.location = location;
        this.type = type;
        this.NoOfYears = NoOfYears;
        this.NoOfEvents = NoOfEvents;
    }
}
