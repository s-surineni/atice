/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package atice;

/**
 *
 * @author umaram
 */
public class MatMulDC {
    int odi=0;
    public static void main(String[] args){
        MatMulDC m1=new MatMulDC();
        //m1.Td2Od(m1.A);
        //m1.Display2D(m1.A);
        int[][] C=m1.SqMatMulDC(m1.A, m1.B);
        m1.Display2D(C);
        
    }
    
    int[][] A={{1,2,3,4},
               {5,6,7,8},
               {9,10,11,12},
               {13,14,15,16}};
    int[][] B=A;
    
    int[][] SqMatMulDC(int A[][],int B[][]){
        
        if(A.length==1){
            int[][] C=new int[1][1];
            C[0][0]=A[0][0]*B[0][0];
            return C;
        }
        else{
            int C[][]=new int[A.length][A.length];
            //System.out.println("lenght of A "+A.length);
            //System.out.println("value of new length "+A.length/2);
            int[][] A11=new int[A.length/2][A.length/2];
            int[][] A12=new int[A.length/2][A.length/2];
            int[][] A21=new int[A.length/2][A.length/2];
            int[][] A22=new int[A.length/2][A.length/2];
            A11=splitArr(A, A11,0,0);
            A12=splitArr(A, A12,0,A12.length);
            A21=splitArr(A, A21,A21.length,0);            
            A22=splitArr(A, A22,A22.length,A22.length);
            
            int[][] B11=new int[A.length/2][A.length/2];
            int[][] B12=new int[A.length/2][A.length/2];
            int[][] B21=new int[A.length/2][A.length/2];
            int[][] B22=new int[A.length/2][A.length/2];
            B11=splitArr(B, B11,0,0);
            B12=splitArr(B, B12,0,A12.length);
            B21=splitArr(B, B21,A21.length,0);            
            B22=splitArr(B, B22,A22.length,A22.length);
                        
            int[][] C11=new int[A.length/2][A.length/2];
            int[][] C12=new int[A.length/2][A.length/2];
            int[][] C21=new int[A.length/2][A.length/2];
            int[][] C22=new int[A.length/2][A.length/2];
            C11=mSum(SqMatMulDC(A11, B11), SqMatMulDC(A12, B21));
            C12=mSum(SqMatMulDC(A11, B12), SqMatMulDC(A12, B22)); 
            C21=mSum(SqMatMulDC(A21, B11), SqMatMulDC(A22, B21));
            C22=mSum(SqMatMulDC(A21, B12), SqMatMulDC(A22, B22));
            Display2D(C11);
            Display2D(C12);
            Display2D(C21);
            Display2D(C22);
            
            C=combiInC(C, C11, 0, 0);
            C=combiInC(C, C12, 0, C12.length);
            C=combiInC(C, C21, C21.length, 0);
            C=combiInC(C, C22, C22.length, C22.length);
            Display2D(C);
            
            return C;
        }
        
    }
    
    
    
    void Display2D(int[][] Arr){
        System.out.println("start of 2d array");
        int rd=Arr.length;
        int cd=Arr.length;
        for(int trk=0;trk<rd;trk++){
         for(int trk1=0;trk1<cd;trk1++)   {
             System.out.print(Arr[trk][trk1]+" ");
         }
         System.out.println();
        }
        System.out.println("end of 2d array");
    }
    
    void Display(int[] Arr){
        System.out.println("Start of Display");
        for(int trk=0;trk<Arr.length;trk++){
         
         System.out.println(Arr[trk]+ " ");
        }
        System.out.println("End of Display");
    }
    
    int[][] splitArr(int[][] A,int B[][],int rs,int cs){
        
        for(int r=0;r<B.length;r++){
            for(int c=0;c<B.length;c++){
                B[r][c]=A[r+rs][c+cs];
            }
        }
        return B;
        
    }
    
    int[][] mSum(int A[][],int B[][]){
        int ind=A.length;
        int[][] C=new int[A.length][A.length];
        for(int r=0;r<ind;r++){
            for(int c=0;c<ind;c++){
                C[r][c]=A[r][c]+B[r][c];
            }
        }
        //Display2D(A);
        return C;
    }
    
    int[][] combiInC(int[][] C,int[][] PC,int rs,int cs){
        /*int ind=A.length;
        for(int r=0;r<ind;r++){
            for(int c=0;c<ind;c++){
                C[odi]=A[r][c];
                odi++;
            }
        }
        odi--;*/
        for(int r=0;r<PC.length;r++){
            for(int c=0;c<PC.length;c++){
                C[r+rs][c+cs]=PC[r][c];
            }
        }
        
        return C;
        
    }
    
    int[][] Od2Td(int ind,int[] A){
        int[][] C=new int[ind][ind];
        for(int r=0;r<ind;r++){
            for(int c=0;c<ind;c++){
                C[r][c]=A[odi];
                odi++;
            }
        }
        odi--;
        return C;
    }
}
