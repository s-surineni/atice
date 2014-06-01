/*
 * 2.3-5
pg 39 binary search using recursion
 */

package atice;

/**
 *
 * @author vinnu
 */
public class binSerachRecurr extends DataSamples{
    
    public static void main(String[] args) {
        //new binSerachRecurr().binSrch(new isort().insort(new DataSamples().getRandomArr(10)), 0, 10, 3);
        int A[]={1,2};
        new binSerachRecurr().binSrch(A, 0,0, 1);
    }
    
    void binSrch(int A[],int s,int e,int v){
        if(s!=e){
            int m = (s+e)/2;
            if(A[m]==v){
                System.out.println(m+1);
                return;
            }
            else if(A[m]>v){
                binSrch(A, s, m-1, v);
            }
            else{
                binSrch(A, m+1, e, v);
            }
        }
        else{
            if(A[s]==v){
                System.out.println(s+1);
            }
            else{
                System.out.println("element not present");
            }
            
        }
    }
}


