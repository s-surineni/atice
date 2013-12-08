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
    int odi=0;
    public static void main(String[] args){
        MAddDivCon m1=new MAddDivCon();
        //m1.Td2Od(m1.A);
        //m1.Display2D(m1.A);
        m1.SqMatMulDC(m1.A, m1.B);
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
            int D[]=Td2Od(A);
            int[][] A11=new int[A.length/2][A.length/2];
            A11=splitArr(D, A11);
            int[][] A12=new int[A.length/2][A.length/2];
            A12=splitArr(D, A12);
            int[][] A21=new int[A.length/2][A.length/2];
            A21=splitArr(D, A21);
            int[][] A22=new int[A.length/2][A.length/2];
            A22=splitArr(D, A22);
            odi=0;
            D=Td2Od(B);
            int[][] B11=new int[A.length/2][A.length/2];
            int[][] B12=new int[A.length/2][A.length/2];
            int[][] B21=new int[A.length/2][A.length/2];
            int[][] B22=new int[A.length/2][A.length/2];
            B11=splitArr(D, B11);
            B12=splitArr(D, B12);
            B21=splitArr(D, B21);
            B22=splitArr(D, B22);
            
            odi=0;
            int[][] C11=new int[A.length/2][A.length/2];
            int[][] C12=new int[A.length/2][A.length/2];
            int[][] C21=new int[A.length/2][A.length/2];
            int[][] C22=new int[A.length/2][A.length/2];
            C11=mSum(SqMatMulDC(A11, B11), SqMatMulDC(A12, B21));
            /*D=combiInC(D,C11);
            C12=mSum(SqMatMulDC(A11, B12), SqMatMulDC(A12, B22));
            D=combiInC(D,C12);
            C21=mSum(SqMatMulDC(A21, B11), SqMatMulDC(A22, B21));
            D=combiInC(D,C21);
            C22=mSum(SqMatMulDC(A21, B12), SqMatMulDC(A22, B22));
            D=combiInC(D,C22);
            odi=0;
            C=Od2Td(C.length,D);
            odi=0;*/
            return C;
        }
        
    }
    
    int[] Td2Od(int[][] A){
        //System.out.println("lenght of a.length "+A.length);
        int D1[]=new int[(A.length)*(A.length)];
        //System.out.println("value of D1 "+D1.length);
        int Odi=0;
        int rci=A.length;
        for(int ri=0;ri<rci;ri++){
            for(int ci=0;ci<rci;ci++){
                D1[Odi]=A[ri][ci];
                Odi++;
                //System.out.println("value of ci+ri " + (ci+ri));
            }
        }
        
        //Display(D1);
        //splitArr(D1);
        return D1;
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
    
    int[][] splitArr(int[] A,int B[][]){
        //Odi=0;
        int ind=(int)Math.sqrt(A.length/4);
        //System.out.println("value of ind "+ind);
        B=new int[ind][ind];
        for(int r=0;r<ind;r++){
            for(int c=0;c<ind;c++){
                B[r][c]=A[odi];
                odi++;
            }
        }
        //Display2D(B);
        return B;
        
    }
    
    int[][] mSum(int A[][],int B[][]){
        int ind=A.length;
        for(int r=0;r<ind;r++){
            for(int c=0;c<ind;c++){
                A[r][c]=A[r][c]+B[r][c];
            }
        }
        Display2D(A);
        return A;
    }
    
    int[] combiInC(int[] C,int[][] A){
        int ind=A.length;
        for(int r=0;r<ind;r++){
            for(int c=0;c<ind;c++){
                C[odi]=A[r][c];
                odi++;
            }
        }
        odi--;
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
