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
    
    void mergesort(int A[],int st,int ed){
        if(st<ed){
           int seg=(st+ed)/2;
            mergesort(A, st, seg);
            mergesort(A, seg+1, ed);
            merge(A,st,seg,ed);
        }
        

}
    void merge(int[] A,int st,int seg,int ed){
        int ll=seg-st+1;
        int rl=ed-seg;
        int La[]=new int[ll+1];
        int Ra[]=new int[rl+1];
        for(int trk=0;trk<ll;trk++,st++){
            La[trk]=A[st++];
        }
        La[La.length-1]=1000;
        seg++;
        for(int trk=0;trk<rl;trk++,seg++){
            Ra[trk]=A[st++];
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
    
}
