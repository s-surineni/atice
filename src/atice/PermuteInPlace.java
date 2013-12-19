/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package atice;

import java.util.Random;

/**
 *
 * @author umaram
 */
public class PermuteInPlace {
    
    public static void main(String[] args){
        PermuteInPlace pip=new PermuteInPlace();
        int A[]={1,2,3,4,5};
        A=pip.justDoIt(A);
        pip.Display(A);
    }
    
    int [] justDoIt(int A[]){
        Random ran=new Random();
        int len=A.length;
        for(int tr=0;tr<len;tr++){
            swap(A,tr,justDoIt(tr, A.length-1));
        }
        return A;
    }
    
    void swap(int[] A,int to,int frm){
        int tem=A[to];
        A[to]=A[frm];
        A[frm]=A[to];
    }
    
    void Display(int[] Arr){
        System.out.println("Start of Display");
        for(int trk=0;trk<Arr.length;trk++){
         
         System.out.println(Arr[trk]+ " ");
        }
        System.out.println("End of Display");
    }
    
    int justDoIt(int min,int max){
        Random rad=new Random();
        int random=rad.nextInt(max-min+1)+min;
        System.out.println("the num generated is "+random);
        return random;
    }
    
}
