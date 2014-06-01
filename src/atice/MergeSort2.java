//this is the second implementattion of merge sort
//doesn't use sentinels
//pg 37 2.3-2
package atice;

/**
 *
 * @author vinnu
 */
public class MergeSort2 {
    public static void main(String[] args){
        MergeSort ms = new MergeSort();
        int RandomArt[] = new DataSamples().getRandomArr(10);
        ms.mergeSort(RandomArt, 0, 9);
    }
    
    void mergeSort(int A[],int strt,int end)
    {
        if(strt < end)
        {
            int mid = (strt + end) /2;
            mergeSort(A, strt, mid);
            mergeSort(A, mid+1, end);
            merge(A, strt, mid, end);
        }
    }
    
    void merge(int A[],int strt,int mid,int end)
    {
        int fhalfSz = mid-strt+1;
        int shalfSz = end -mid;
        int[] fHalf = new int [fhalfSz];
        int[] sHalf = new int[shalfSz];        
        
        for(int i = 0 ; i<fhalfSz;i++)
        {
            fHalf[i] = A[strt+i];
        }
                
        for(int i = 0 ; i<shalfSz;i++)
        {
            sHalf[i] = A[mid+i+1];
        }
        int fInd= 0;
        int sInd= 0;
        for( ;strt<=end;strt++)
        {
            if(fInd<fhalfSz && sInd <shalfSz){
                if(fHalf[fInd]<sHalf[sInd])
                {
                A[strt] = fHalf[fInd];
                fInd++;
                }
            }
            else if(sInd <shalfSz)
            {
                A[strt] = sHalf[sInd];
                sInd++;
            }
            else
            {
                A[strt] = fHalf[fInd];
                fInd++;
            }
        }
        new JavaL().display(A);
    }
    
}
