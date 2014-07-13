/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package atice;

/**
 *
 * @author umaram
 */
public class MaxSubArray {
    
    int lo,hi,su;
    static JavaL jl;
    
    public static void main(String[] args){
        jl = new JavaL();
        int A[]={-11,-2,-3,-4};
        MaxSubArray m=new MaxSubArray();
        //m.maxCrossSubArr(A,0,A.length-1);
        int rets[]=m.maxRecSubArr(A, 1, A.length);
        jl.display(rets);
    }
    int[] maxCrossSubArr(int A[],int low,int high){
        
        //int A[]={13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7};
        low--;
        high--;
        int midd=((low+high)/2);
        //System.out.println("middle index "+midd);
        int leftsum=1<<31;
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
        int rightsum=1<<31;
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
        int Arr[]={lo,hi,leftsum+rightsum};
        return Arr;
}
    
    int[] maxRecSubArr(int A[],int low,int high){
        //int l,h,s;
        low--;
        high--;
        if(high==low){
            ++low;
            int Ar[]={low,low,A[high]};
            return Ar;
        }
        int mid=((low+high)/2)+1;
        int lA[]=maxRecSubArr(A, ++low, mid);
        jl.display(lA);
        int hA[]=maxRecSubArr(A, mid+1, ++high);
        jl.display(hA);
        int cA[]=maxCrossSubArr(A, low, high);
        jl.display(cA);
        if(lA[2]>hA[2]){
            if(lA[2]>cA[2])
            return lA;
            else
               return cA;
        }
        else if(hA[2]>cA[2]){
            return hA;
        }
        else return cA;
    }
}

