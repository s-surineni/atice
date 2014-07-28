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
    int A[] = new DataSamples().getRandomArr(10);
    public static void main(String[] args)
    {
        MaxPriQ mp = new MaxPriQ();
        mp.begin();
        
    }
    
    void begin()
    {
        JavaL jl = new JavaL();
        jl.display(A);
        buildMaxHeap();
        jl.display(A);
//        for (int i = 0; i < 10; i++) 
//        {
//            System.out.println(extractMax());
//        }
//        System.out.println("inserting");
//        for (int i = 0; i < 11; i++) {
//            insert(i);
//        }
//        jl.display(A);
//        System.out.println("extracting");
//        for (int i = 0; i < 11; i++) 
//        {
//            System.out.println(extractMax());
//        }
    }
    
    int maximum()
    {
        System.out.println("in maximum "+A[0]);
        return A[0];
    }
    
//    void insert(int ele){
//        if(heapLen>=A.length)
//        {
//            System.out.println("Heap is full");
//        }
//        else
//        {
//            A[heapLen] = ele;
//            heapLen++;
//            maxHeapify(heapLen);
//            
//        }
//    }
    
    void extractMax()
    {
        if(heapLen >=1)
        {
            int max = A[0];
            exchange(A, 0, heapLen-1);
            heapLen--;
            maxHeapify( 1);
            System.out.println(max);
        }
        else 
        {
            System.out.println("heap is empty"); 
        }
        
    }
    
    private void buildMaxHeap()
    {
        heapLen = A.length;
        for(int i = (A.length/2)-1;i>=0;i--)
        {
            maxHeapify(i);
        }
    }
    
    private void maxHeapify(int ind)
    {
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
            maxHeapify( largest);
        }
    }
    
    private void exchange(int A[],int to,int frm)
    {
        int tmp = A[to];
        A[to]=A[frm];
        A[frm] = tmp;
    }
}
