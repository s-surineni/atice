/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package atice;

/**
 *
 * @author vinnu
 */
class MergeSort
{
    
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
        int fhalf = mid-strt+1;
        int shalf = end -mid;
        int[] rHalf = new int[shalf+1];
        int[] lHalf = new int [fhalf+1];
        
        for(int i = 0 ; i<fhalf;i++)
        {
            lHalf[i] = A[strt+i];
        }
        int large = -1>>>1;
        lHalf[fhalf] = large;
        
        for(int i = 0 ; i<shalf;i++)
        {
            rHalf[i] = A[mid+i+1];
        }
        rHalf[shalf] = large;
        int lInd= 0;
        int rInd= 0;
        for( ;strt<=end;strt++)
        {
            if(rHalf[rInd]<lHalf[lInd])
            {
                A[strt] = rHalf[rInd];
                rInd++;
            }
            else
            {
                A[strt] = lHalf[lInd];
                lInd++;
            }
        }
        new JavaL().display(A);
    }
}