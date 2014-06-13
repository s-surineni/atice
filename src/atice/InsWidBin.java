//2.3-6 insertion sort combined with binary search

package atice;

/**
 *
 * @author vinnu
 */
public class InsWidBin {
    BinarySearch bs = new BinarySearch();
    JavaL jl = new JavaL();
    public static void main(String[] args) {
        InsWidBin iwb = new InsWidBin();
        int A[] = new DataSamples().getRandomArr(10);
        //int A[] = {5,4};
        iwb.doInsert(A, 10);
    }
    
    void doInsert(int A[],int size){
        jl.display(A);
        for(int i=1;i<size;i++){
            int curIn = i;
            int curEl = A[i];
            int pos = bs.binSrch(A, i+1, A[i]);
            if(A[pos]<curEl){
                pos++;
            }
            for( ; curIn>pos ;curIn-- )
            {
                A[curIn] = A[curIn-1];
            }
            A[curIn]=curEl;
        }
        new JavaL().display(A);
    }
}
