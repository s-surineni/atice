//2.3-4 cormen 
//recursive implementation of insertion sort

package atice;

/**
 *
 * @author vinnu
 */
public class IsortRecurr {
    public static void main(String[] args) {
        
        IsortRecurr ir= new IsortRecurr();
        int RandomArt[] = new DataSamples().getRandomArr(10);
        ir.iSort(RandomArt);
        new JavaL().display(RandomArt);
        
    }
    
    void iSort(int A[]){
        iRecur(A, 1);
        new JavaL().display(A);
    }
    
    void iRecur(int A[],int lim){
        if(lim<A.length){
            int next=lim+1;
            int last = A[lim];
            for( ;lim>0 && last<A[lim-1];lim--){
                A[lim]=A[lim-1];
            }
            A[lim] = last;
            iRecur(A, next);
        }
    }
}
