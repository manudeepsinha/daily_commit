class MergeSort {

    void merge(int arr[], int left, int mid, int right) {

        //find size of the two subarrays to be merged
        int a1 = mid+1 - left;
        int a2 = right - mid;

        //creating temp arrays
        int L[] = new int [a1];
        int R[] = new int [a2];

        //copying data to temp arrays
        for (int i=0; i<a1; ++i)
            L[i] = arr[left+i];

        for (int i=0; i<a2; ++i)
            R[i] = arr[mid+left+i];

        //merge the temp arrays

            //initial indexes of sub arrays
        int i = 0, j = 0;
            //initialize index of merged subarray array
        while (i<n1 && j<n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            }
            else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        //copying remaining elements of L[], if any
        while (i < n1) {

            arr[k] = L[i];
            i++;
            k++;
        }

        //copying remaining elements of R[], if any
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }

    }//end of merge method

    static void sort(int arr[], int left, int right) {

        if (left < right) {
            //find middle point
            int mid = (left + right) / 2;

            //sort first and second halves
            sort(arr,left,mid);
            sort(arr,mid+1,right);

            //merge the sorted halves
            merge(arr,left,mid,right);
        }
    }

    void printArray(int arr[]) {

        for(int item:arr) {
            System.out.print(item + " ");
        }
        System.out.println();
    }//end of printArray method

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
            sort(arr,0,arr.length-1);
            System.out.println("Array after sorting:");
            printArray(arr);
        }//end of if condition
        else
            System.out.println("Array length is 0 or invalid.");
       
        in.close();

    }//end of main method
}//end of class MergeSort