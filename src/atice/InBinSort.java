/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package atice;

/**
 *
 * @author vinnu
 */
public class InBinSort {
    
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
