/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package atice;

/**
 *
 * @author vinnu
 */
public class BinarySearch {
    public static void main(String[] args){
        int A[]={1,2,3};
        BinarySearch b1=new BinarySearch();
        if(A[b1.binSrch(A, 3, 1)]==1){
            System.out.println("found" );
        }
        else{
            System.out.println("the element has not found");
        }
    }
    int binSrch(int A[],int size,int x){
        int low,up,mid;
        low=1;
        up=size;
        
        do{
           mid=(low+up)/2;
           if(x>A[mid-1]){
               low=mid+1;
           }
           else{
               up=mid-1;
           }
        }while(A[mid-1]!=x && low<=up);
        
        return mid-1;
    }
}
