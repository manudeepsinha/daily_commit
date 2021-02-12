import java.util*

public class Test {

    public static void main(String[] args) {

        int arr[][] = new int arr[4][];
        arr[0] = new int[1];
        arr[1] = new int[2];
        arr[2] = new int[3];
        arr[3] = new int[4];

        int i,j,k = 0;
        for (i = 0; i < 4; i++) {
            for (j = 0; j < i; j++) {
                arr[i][j] = k;
                k++;
            }
        }
        for (i = 0; i < 4; i++) {
            for (j = 0; j < i; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }

    }
}