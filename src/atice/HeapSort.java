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
    
    public static void main(String[] args){
        int A[]={4,6,2};
        HeapSort h1=new HeapSort();
        h1.heapify(A, 0);
    }
    void heapify(int A[],int i){
        int largest=0;
        int lChild=leftChil(i);
        int rChild=rightChil(i);
        if(lChild<A.length ) {
            if(A[lChild]>A[i]){
            largest=lChild;
        }
        }
        else
            largest=i;
        if(rChild<A.length ){
            if(A[rChild]>A[largest]){
            largest=rChild;
            }
        }
        if(largest!=i){
            swap(A, i, largest);
            heapify(A, largest);
        }

}
    
    int leftChil(int parent){
        return 2*parent+1;
    }
    int rightChil(int parent){
        return 2*parent+2;
    }
    
    void swap(int A[],int par,int chil){
        int temp=A[par];
        A[par]=A[chil];
        A[chil]=temp;
    }
    
}

