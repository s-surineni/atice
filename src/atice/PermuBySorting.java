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
public class PermuBySorting {
    public static void main(String[] args){
        PermuBySorting pp=new PermuBySorting();
        int A[]={1,2,3,4,5};
        A=pp.doIt(A);
        pp.Display(A);
    }
    
    int [] doIt(int[] A){
        int lenofA=A.length;
        int[] Prios=new int[lenofA];
        for(int tr=0;tr<lenofA;tr++){
            Prios[tr]=ranDom(1, lenofA*lenofA*lenofA);
        }
        Display(Prios);
        A=sortWidPri(A,Prios);
        return A;
    }
    
    int[] sortWidPri(int A[], int Pri[]) {
        int max = 0;
        for (int tr = 0; tr < Pri.length; tr++) {
            if (max < Pri[tr]) {
                max = Pri[tr];
            }
        }
        max++;
        int B[] = new int[A.length];
        for (int tro = 0; tro < A.length; tro++) {
            int least = Pri[0];
            int lind = 0;
            for (int tr = 1; tr < Pri.length; tr++) {
                if (least > Pri[tr]) {
                    least = Pri[tr];
                    lind = tr;
                }
            }
            B[tro]=A[lind];
            Pri[lind]=max;
        }
        return B;
    }
    int ranDom(int min,int max){
        Random rad=new Random();
        int random=rad.nextInt(max-min+1)+min;
        
        return random;
    }
    
    void Display(int[] Arr) {
        System.out.println("Start of Display");
        for(int trk = 0; trk < Arr.length; trk++) {

            System.out.println(Arr[trk] + " ");
        }
        System.out.println("End of Display");
    }
}
