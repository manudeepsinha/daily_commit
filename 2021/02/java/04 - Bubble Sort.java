//Implementation code of bubble sort
import java.util.*
class BubbleSort {

    //sorting the array using bubble sort
    void bubbleSort(int arr[]) {

        int n = arr.length;
        boolean swapped;
        for(int i = 0; i < n-1; i++) {  //denotes pass #
            for(int j = 0; j < n-i-1; j++) { //denotes element in the pass
                if(arr[j] > arr[j+1]) {
                    //swapping of the element
                    arr[j] += arr[j+1];
                    arr[j+1] = arr[j] - arr[j+1];
                    arr[j] -= arr[j+1];
                    swapped = true;

                } //end of if block
            }//end of element checking loop
            //if no 2 elements were swapped by inner loop, then break
            if (swapped == false)
                break;
        }//end of pass loop
    }

    //to print the array
    void printArray(int arr[]) {

        //enhanced for loop
        for (int item:arr) {
            System.out.print(item + " ");
        }
        System.out.println();
    }

    //driver method
    public static void main(String[] args) {

        int arr[]; //say {64,34,25,12,22,11,90};
        int nums;
        Scanner in = new Scanner(System.in);
        System.out.print("Enter the number of elements to insert in the array: ");
        nums = in.nextInt();
        arr = new arr[nums];

        if(arr.length > 0) {
            System.out.println("Enter the value of all the items, space seperated:");
            for(int i = 0; i < arr.length; ++i) {
                arr[i] = in.nextInt();
            }

            System.out.println("Array before sorting:");
            printArray(arr);
            bubbleSort(arr);
            System.out.println("Array after sorting:");
            printArray(arr);
        }//end of if condition
        else
            System.out.println("Array length is 0 or invalid.");
       
        in.close();

    }//end of main method
}//end of class BubbleSort