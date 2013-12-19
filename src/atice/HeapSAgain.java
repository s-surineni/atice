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
        int A[]={6,7,8};
        ha.hepify(A, 0);
        ha.Display(A);
        
    }
    
    void hepify(int A[],int ind){
        int largest=0;
        int lc=lChild(ind);
        int rc=rChild(ind);
        int heapSize=A.length;
        if(lc<heapSize && A[lc]>A[ind]){
            largest=lc;
        }
        else
            largest=ind;
        if(rc<heapSize && A[rc]>A[ind]){
            largest=rc;
        }
        if(largest != ind){
            swap(A,ind,largest);
            hepify(A, largest);
        }
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
