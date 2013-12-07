/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package atice;

/**
 *
 * @author umaram
 */
public class Maxsubarray {
    
    int lo,hi,su;
    
    public static void main(String[] args){
        int A[]={-1,-2,5,-4,7,-1,-1,-2,9,16};
        Maxsubarray m=new Maxsubarray();
        //m.maxCrossSubArr(A,0,A.length-1);
        int rets=m.maxRecSubArr(A, 0, A.length-1);
        System.out.println(rets);
    }
    int maxCrossSubArr(int A[],int low,int high){
        
        //int A[]={13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7};
        int midd=(low+high)/2;
        //System.out.println("middle index "+midd);
        int leftsum=-1000;
        int sum=0;
        int maxleft=0;
        for(int i=midd;i>=0;i--){
            sum=sum+A[i];
            if(leftsum<sum){
                leftsum=sum;
                maxleft=i;
            }
        }
        lo=maxleft+1;
        int rightsum=-1000;
        sum=0;
        int maxr=0;
        for(int i=midd+1;i<=A.length-1;i++){
            sum=sum+A[i];
            if(rightsum<sum){
                rightsum=sum;
                maxr=i;
            }
        }
        hi=maxr+1;
        return su=leftsum+rightsum;
}
    
    int maxRecSubArr(int A[],int low,int high){
        //int l,h,s;
        if(high==low){
            //l=low;h=high;s=A[low];
            return A[low];
        }
        int mid=(low+high)/2;
        int ll,lh,ls;
        maxRecSubArr(A, low, mid);
        maxRecSubArr(A, mid+1, high);
        maxCrossSubArr(A, low, high);
        if(maxRecSubArr(A, low, mid)>maxRecSubArr(A, mid+1, high)){
            if(maxRecSubArr(A, low, mid)>maxCrossSubArr(A, low, high))
            return maxRecSubArr(A, low, mid);
            else
               return maxCrossSubArr(A, low, high);
        }
        else if(maxRecSubArr(A, mid+1, high)>maxCrossSubArr(A, low, high)){
            return maxRecSubArr(A, mid+1, high);
        }
        else return maxCrossSubArr(A, low, high);
    }
}

