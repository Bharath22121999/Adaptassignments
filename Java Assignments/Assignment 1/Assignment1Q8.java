class BubbleSort{

    public int[] bubbleSort(int arr[]) {
    	for(int i=0;i<arr.length;i++) {
    		for(int j=1;j<arr.length-i;j++) {
    			if(arr[j-1]>arr[j]) {
    				int t = arr[j-1];
    				arr[j-1] = arr[j];
    				arr[j] = t;
    			}
    		}
    	}
    	return arr;
    }
}
public class Assignment1Q8 {
    public static void main(String args[]) {
        int arr[] = {5,12,14,6,78,19,1,23,26,35,37,7,52,86,47};
    }
}