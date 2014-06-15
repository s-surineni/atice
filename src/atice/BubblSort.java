/*
2-2 bubble sort correct
 the inner loop makes sure that elements after 
j are greater than A[j]
the outer loop makes sure that after each iteration 
the 'i' smallest elements are arranged in 
asending order

 */

package atice;

/**
 *
 * @author vinnu
 */
public class BubblSort {
    JavaL jl = new JavaL();
    
    
    public static void main(String[] args) {
        BubblSort bs = new BubblSort();
        DataSamples ds = new DataSamples();
        int Arr[] = ds.getRandomArr(10);
        bs.bubbly(Arr,10);
    }
    
    void bubbly(int A[],int len){
        jl.display(A);
        for(int i=0;i<len-1;i++)
        {
            for(int j = len-1;j>=i+1;j--){
                if(A[j]<A[j-1]){
                    int temp = A[j];
                    A[j] = A[j-1];
                    A[j-1]=temp;
                }
            }
        }
        jl.display(A);
    }
    
}
