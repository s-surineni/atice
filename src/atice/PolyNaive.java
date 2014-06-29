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
public class PolyNaive {
    
    public static void main(String[] args) {
        DataSamples jl = new DataSamples();
        JavaL jl2 = new JavaL();
        int A[] = jl.getRandomArr(3);
        new PolyNaive().calc(A, 2);
        jl2.display(A);
    }
    
    void calc(int A[],int x){
        int len =A.length;
        int sum = 0;
        for(int i =0 ;i<len;i++)
        {
            int z =1;
            for(int j = 1;j<=i;j++){
                z = z*x;
                
            }
            int curr = A[i]*z;
            sum += curr;
        }
        
        System.out.println("the output is "+sum);

    }
}

