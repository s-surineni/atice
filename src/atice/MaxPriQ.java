/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package atice;

/**
 *
 * @author simpli
 */
public class MaxPriQ {
    int heapLen;
    public static void main(String[] args)
    {
        JavaL jl = new JavaL();
        MaxPriQ mp = new MaxPriQ();
        int A[] = new DataSamples().getRandomArr(10);
        //int A[] = {1,2,3,4,5};
        jl.display(A);
        mp.buildMaxHeap(A);
        jl.display(A);
        for (int i = 0; i < 10; i++) {
            System.out.println(mp.extractMax(A));
        }
    }
    
    int maximum(int A[])
    {
        return A[0];
    }
    
    int extractMax(int A[])
    {
        int max = A[0];
        exchange(A, 0, heapLen-1);
        heapLen--;
        maxHeapify(A, 1);
        return max;
    }
    
    private void buildMaxHeap(int A[])
    {
        heapLen = A.length;
        for(int i = A.length/2;i>0;i--)
        {
            maxHeapify(A,i);
        }
    }
    
    private void maxHeapify(int A[],int ind)
    {
        ind--;
        int lI = 2*ind+1;
        int rI = 2*ind+2;
        int largest = ind;
        if(lI<heapLen && A[lI] > A[ind])
        {
            largest = lI;
        }
        if(rI<heapLen && A[rI] > A[largest])
        {
            largest = rI;
        }
        if(largest != ind)
        {
            exchange(A, largest, ind);
            maxHeapify(A, largest+1);
        }
    }
    
    private void exchange(int A[],int to,int frm)
    {
        int tmp = A[to];
        A[to]=A[frm];
        A[frm] = tmp;
    }
}
