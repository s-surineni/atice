/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package atice;

/**
 *
 * @author umaram
 */
public class MAddDivCon {
    
    int[][] A={{1,2,3,4},
               {5,6,7,8},
               {9,10,11,12},
               {13,14,15,16}};
    int[][] B=A;
    /*
    int[][] SqMatMulDC(int A[][],int B[][]){
        
        if(A.length==1){
            int[][] C=new int[1][1];
            C[0][0]=A[0][0]*B[0][0];
        }
        else{
            int[][] A11=new int[(int)Math.sqrt(A.length/(4))][(int)Math.sqrt(A.length/(4))];
            int[][] A12=new int[(int)Math.sqrt(A.length/(4))][(int)Math.sqrt(A.length/(4))];
            int[][] A21=new int[(int)Math.sqrt(A.length/(4))][(int)Math.sqrt(A.length/(4))];
            int[][] A22=new int[(int)Math.sqrt(A.length/(4))][(int)Math.sqrt(A.length/(4))];
            
            int[][] B11=new int[(int)Math.sqrt(A.length/(4))][(int)Math.sqrt(A.length/(4))];
            int[][] B12=new int[(int)Math.sqrt(A.length/(4))][(int)Math.sqrt(A.length/(4))];
            int[][] B21=new int[(int)Math.sqrt(A.length/(4))][(int)Math.sqrt(A.length/(4))];
            int[][] B22=new int[(int)Math.sqrt(A.length/(4))][(int)Math.sqrt(A.length/(4))];
            
            int[][] C11=new int[(int)Math.sqrt(A.length/(4))][(int)Math.sqrt(A.length/(4))];
            int[][] C12=new int[(int)Math.sqrt(A.length/(4))][(int)Math.sqrt(A.length/(4))];
            int[][] C21=new int[(int)Math.sqrt(A.length/(4))][(int)Math.sqrt(A.length/(4))];
            int[][] C22=new int[(int)Math.sqrt(A.length/(4))][(int)Math.sqrt(A.length/(4))];
        }
        return C;
    }*/
    
    void Td2Od(int[][] A){
        int D1[]=new int[A.length];
        int rci=(int)Math.sqrt(A.length);
        for(int ri=0;ri<rci;ri++){
            for(int ci=0;ci<rci;ci++){
                D1[ci+ri]=A[ri][ci];
            }
        }
    }
}
