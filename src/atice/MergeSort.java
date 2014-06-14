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
        new JavaL().display(RandomArt);
        ms.mergeSort2(RandomArt, 0, 9);
        new JavaL().display(RandomArt);
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
        int[] fHalf = new int [fhalfSz+1];
        int[] sHalf = new int[shalfSz+1];        
        
        for(int i = 0 ; i<fhalfSz;i++)
        {
            fHalf[i] = A[strt+i];
        }
        int large = -1>>>1;
        fHalf[fhalfSz] = large;
        
        for(int i = 0 ; i<shalfSz;i++)
        {
            sHalf[i] = A[mid+i+1];
        }
        sHalf[shalfSz] = large;
        int fInd= 0;
        int sInd= 0;
        for( ;strt<=end;strt++)
        {
            if(fHalf[fInd]<sHalf[sInd])
            {
                A[strt] = fHalf[fInd];
                fInd++;
            }
            else
            {
                A[strt] = sHalf[sInd];
                sInd++;
            }
        }
        //new JavaL().display(A);
    }
    //new kind of merge sort 2-1
    void mergeSort2(int A[],int strt,int end){
        Isort is = new Isort();
        if(end -strt>2)
        {
            int mid = (strt + end) /2;
            mergeSort(A, strt, mid);
            mergeSort(A, mid+1, end);
            merge(A, strt, mid, end);
        }
        else{
            is.inSort(A, strt, end);
        }
        
    }
}