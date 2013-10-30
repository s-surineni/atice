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
   static int msin=1;
   static int imid,istart,iend;
    public static void main(String[] args){
        
        MergeSort ms=new MergeSort();
        //ms.Display(Arr);
        ms.mSort(Arr, 0,9);
       // ms.Display(Arr);
    }
    void merge(int Arr[],int start,int mid,int end){
int n1=mid-start+2;
int n2=end-mid+1;
int L[]=new int[n1+1];
int R[]=new int[n2+1];
int trk;
for(trk=0;trk<n1;trk++){
    L[trk]=Arr[start+trk+1-1];
}
int trk2;
for(trk2=0;trk2<n2;trk2++){
    R[trk2]=Arr[mid+trk2];
}
L[n1]=100;
R[n2]=100;
trk=1;
trk2=1;
int trk3;
for(trk3=start;trk3<end;trk3++){
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
        istart=start;
        iend=end;
        if(start<end){
           // System.err.println("start mind end "+istart+" "+imid+" "+iend+" ");
            int mid=(start+end)/2;
            imid=mid;
            mSort(Arr, start, mid);
            mSort(Arr, mid+1, end);
            mergeDup(Arr, start, mid, end);
        }
    }
    
    void Display(int[] Arr){
        for(int trk=0;trk<Arr.length;trk++){
         System.out.println(Arr[trk]);
         System.out.println();
        }
    }
    
    void mergeDup(int[] Arr,int start,int mid,int end){
        System.err.println("start "+start +" mid "+mid+" end "+end);
    }
}

