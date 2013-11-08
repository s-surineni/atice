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
        int A[]={4,2,6,8,7,9,11};
        
        HeapSort h1=new HeapSort();
        h1.Display(A);
        //h1.heapify(A, 0);
        h1.buildHead(A);
        h1.Display(A);
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
    
    void Display(int[] Arr){
        System.out.println("Start of Display");
        for(int trk=0;trk<Arr.length;trk++){
         
         System.out.println(Arr[trk]+ " ");
        }
        System.out.println("End of Display");
    }
    
    int[] buildHead(int A[]){
        for(int nonL=A.length/2-1;nonL>=0;nonL-- ){
            heapify(A, nonL);
        }
        return A;
    }
    
}

