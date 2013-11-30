/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package atice;

/**
 *
 * @author umaram
 */
public class BubbleSort {
    public static void main(String[] args){
        BubbleSort b1=new BubbleSort();
        int A[]={5,2,1,9,6,8,4,5};
        A=b1.bubble(A);
        b1.Display(A);
    }
    
    int[] bubble(int A[]){
for(int i=0;i<A.length-1;i++){
for(int j=A.length-1;j>0;j--){
    if(A[j]<A[j-1]){
        swap(A,j,j-1);
    }
}
}
return A;
}
    void swap(int[] A,int frm,int to){
        int temp=A[frm];
        A[frm]=A[to];
        A[to]=temp;
    }
    
    void Display(int[] Arr){
        System.out.println("Start of Display");
        for(int trk=0;trk<Arr.length;trk++){
         
         System.out.println(Arr[trk]+ " ");
        }
        System.out.println("End of Display");
    }
}

