//this program is to use insertion sort
package atice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

/**
 *
 * @author vinnu
 */
public class isort {
    public static void main(String[] args) throws IOException {
        isort is=new isort();
        is.tInput();
        
    }
    
    void start() throws IOException{
        
    }
    void tInput(){
        System.out.println("enter the number of elements you want to sort");
        Scanner s1=new Scanner(System.in);
        int size=s1.nextInt();
        System.out.println("start giving input");
        int[] Ar=new int[size];
        for(int i=0;i<size;i++){
            Ar[i]=s1.nextInt();
            
        }
        System.out.println("your input");
        Display(Ar);
        insort(Ar);
    }
    void Display(int[] Arr){
        System.out.println("Start of Display");
        for(int trk=0;trk<Arr.length;trk++){
         
         System.out.println(Arr[trk]+ " ");
        }
        System.out.println("End of Display");
    }
    
    int[] insort(int Arr[]){
        for(int out=1;out<Arr.length;out++){
            
            int key=Arr[out];
            int i=out-1;
            while(i>=0 && Arr[i]>key){
                Arr[i+1]=Arr[i];
                i--;
                Arr[i+1]=key;
            }
            
            
            Display(Arr);
            
        }
        System.out.println("after sorting");
        Display(Arr);
        return Arr;
    }
    
}
