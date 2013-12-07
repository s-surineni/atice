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
    public static void main(String[] args){
        MAddDivCon m1=new MAddDivCon();
        m1.Td2Od(m1.A);
        //m1.Display2D(m1.A);
    }
    
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
        System.out.println("lenght of a.length "+A.length);
        int D1[]=new int[(A.length)*(A.length)];
        System.out.println("value of D1 "+D1.length);
        int Odi=0;
        int rci=A.length;
        for(int ri=0;ri<rci;ri++){
            for(int ci=0;ci<rci;ci++){
                D1[Odi]=A[ri][ci];
                Odi++;
                //System.out.println("value of ci+ri " + (ci+ri));
            }
        }
        Display(D1);
        splitArr(D1);
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
    
    void splitArr(int[] A){
        int Odi=0;
        int ind=(int)Math.sqrt(A.length/4);
        System.out.println("value of ind "+ind);
        int[][] B=new int[ind][ind];
        for(int r=0;r<ind;r++){
            for(int c=0;c<ind;c++){
                B[r][c]=A[Odi];
                Odi++;
            }
        }
        Display2D(B);
    }
}
