/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package atice;

/**
 *
 * @author umaram
 */
public class Magain {
    public static void main(String[] args){
        Magain m1=new Magain();
        int A[]={7,6,8,2,5,9,1,0};
        int D[]=m1.mergesort(A, 0, A.length-1);
        m1.Display(D);
    }
    
    int[] mergesort(int A[],int st,int ed){
        if(st<ed){
           int seg=(st+ed)/2;
            mergesort(A, st, seg);
            mergesort(A, seg+1, ed);
            merge(A,st,seg,ed);
        }
        
return A;
}
    void merge(int[] A,int st,int seg,int ed){
        System.out.println("st passed "+st);
        int ll=seg-st+1;
        int rl=ed-seg;
        int La[]=new int[ll+1];
        int Ra[]=new int[rl+1];
        int trk=0;
        for(;trk<ll;trk++,st++){
            La[trk]=A[st];
        }
        st=st-trk;
        System.out.println("st now "+st);
        La[La.length-1]=1000;
        seg++;
        for(trk=0;trk<rl;trk++,seg++){
            Ra[trk]=A[seg];
        }
        Ra[Ra.length-1]=1000;
        ll=rl=0;
        for(;st<=ed;st++){
            if(La[ll]<=Ra[rl]){
                A[st]=La[ll];
                ll++;
            }
            else{
                A[st]=Ra[rl];
                rl++;
            }
        }
        
    }
    void Display(int[] Arr){
        System.out.println("Start of Display");
        for(int trk=0;trk<Arr.length;trk++){
         
         System.out.println(Arr[trk]+ " ");
        }
        System.out.println("End of Display");
    }
    
}
