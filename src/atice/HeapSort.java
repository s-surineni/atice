/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package atice;

/**
 *
 * @author vinnu
 */
public class HeapSort {
    
    
    public static void main(String[] args) {
        JavaL jl = new JavaL();
        int A[] = new DataSamples().getRandomArr(10);
        jl.display(A);
        HeapSort hs = new HeapSort();
        hs.heapSort(A);        
        jl.display(A);
    }
    
    void maxHeapify(int A[],int ind,int len)
    {
        int largest = ind;
        int lC = (ind<<1)+1;
        int rC = (ind<<1) + 2;
        
        if(lC<=len && A[lC]>A[ind])
        {
            largest = lC;
        }
        if(rC<=len && A[rC]>A[largest])
        {
            largest = rC;
        }
        if(largest!=ind)
        {
            swap(A, largest, ind);
            maxHeapify(A, largest, len);
        }
    }
    
    void buildMaxHeap(int A[])
    {
        for(int i = (A.length/2)-1;i>=0;i--)
        {
            maxHeapify(A, i, A.length-1);
        }
    }
    
    void heapSort(int A[]){
        buildMaxHeap(A);
        for(int i = A.length-1; i>=0;i--)
        {
            swap(A,0,i);
            maxHeapify(A, 0, i-1);
        }
    }
    void swap(int A[],int t,int f)
    {
        int tmp = A[t];
        A[t] = A[f];
        A[f] = tmp;
    }
}

