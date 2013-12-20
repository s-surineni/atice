/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package atice;

/**
 *
 * @author umaram
 */
public class HeapSAgain {
    
    public static void main(String[] args){
        HeapSAgain ha=new HeapSAgain();
        int A[]={1,2,3,6,7,8,9,10};
        ha.heapSort(A);
        ha.Display(A);
        
    }
    
    void heapSort(int A[]){
        buildHeap(A);
        for(int i=A.length-1,j=1;i>=1;i--,j++){
            exch(A,i,0);
            heapify(A, 0,A.length-j);
        }
    }
    
    void buildHeap(int A[]){
        int heapSize=A.length;
        for(int i=(heapSize/2)-1;i>=0;i--){
            heapify(A, i,heapSize);
        }
    }
    
    void heapify(int A[],int ind,int hlen){
        int largest;
        int lc=lChild(ind);
        int rc=rChild(ind);
        int heapSize=hlen;
        if(lc<heapSize && A[lc]>A[ind]){
            largest=lc;
        }
        else
            largest=ind;
        if(rc<heapSize && A[rc]>A[largest]){
            largest=rc;
        }
        if(largest != ind){
            swap(A,ind,largest);
            heapify(A, largest,hlen);
        }
    }
    
    void exch(int A[],int to,int frm){
        A[to]=A[to]+A[frm];
        A[frm]=A[to]-A[frm];
        A[to]=A[to]-A[frm];
    }
    
    void swap(int A[],int to,int frm){
        A[to]=A[to]+A[frm];
        A[frm]=A[to]-A[frm];
        A[to]=A[to]-A[frm];
    }
    
    int parInd(int i){
        return (i-1)/2;
    }
    
    int lChild(int i){
        return (2*i)+1;
    }
    
    int rChild(int i){
        return (2*i)+2;
    }
    
    void Display(int[] Arr) {
        System.out.println("Start of Display");
        for (int trk = 0; trk < Arr.length; trk++) {
            System.out.println(Arr[trk] + " ");
        }
        System.out.println("End of Display");
    }
}
