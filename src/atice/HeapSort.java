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
        int A[]={4,2,6,8,7,9,1};
        //int A[]={3,2,1,5,6};
        
        HeapSort h1=new HeapSort();
        h1.Display(A);
        h1.heapify(A, 0,5);
        //h1.buildHead(A);
        //h1.hpSort(A);
        h1.Display(A);
    }
    void heapify(int A[],int i,int heapLen){
        int largest=i;
        int lChild=leftChil(i);
        int rChild=rightChil(i);
        if(lChild<heapLen ) {
            if(A[lChild]>A[i]){
            largest=lChild;
        }
        }
        else{
            largest=i;}
        if(rChild<heapLen ){
            if(A[rChild]>A[largest]){
            largest=rChild;
            }
        }
        if(largest!=i){
            swap(A, i, largest);
            heapify(A, largest,heapLen);
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
            heapify(A, nonL,A.length);
        }
        return A;
    }
    
    void hpSort(int A[]){
        buildHead(A);
        //Display(A);
        int heapSiz=A.length;
        for(int i=A.length-1;i>=1;i--){
            swap(A, 0, i);
            //Display(A);
            //System.out.println("after swap");
            heapSiz--;
            heapify(A, 0,heapSiz);
            //Display(A);
            //System.out.println("after heapify");
        }
        
    }
    
}

