/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package atice;

/**
 *
 * @author vinnu
 */
public class MergeSort {
   static int Arr[]={2,3,6,1,9,0,4,5,8,7};
    public static void main(String[] args){
        MergeSort ms=new MergeSort();
        ms.mSort(Arr, 0, 9);
    }
    void merge(int Arr[],int start,int mid,int end){
int n1=mid-start+1;
int n2=end-mid;
int L[]=new int[n1+1];
int R[]=new int[n2+1];
int trk;
for(trk=0;trk<n1;trk++){
    L[trk]=Arr[start+trk-1];
}
int trk2;
for(trk2=0;trk2<n2;trk2++){
    R[trk2]=Arr[mid+trk2];
}
L[n1+1]=100;
R[n2+1]=100;
trk=1;
trk2=1;
int trk3;
for(trk3=start;trk3<=end;trk3++){
    if(L[trk]<=R[trk2]){
        Arr[trk3]=L[trk];
        trk++;
    }
    else if(Arr[trk3]==R[trk2]){
    trk2++;
}
}
}
    
    void mSort(int Arr[],int start,int end){
        if(start<end){
            int mid=(start+end)/2;
            mSort(Arr, start, mid);
            mSort(Arr, mid+1, end);
            merge(Arr, start, mid, end);
        }
    }
}

