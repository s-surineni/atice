/*
 * this class tells how to take input from terminal
 * using scanner class
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

/**
 *
 * @author vinnu
 */
public class JavaL {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        JavaL j1=new JavaL();
        j1.tInput();
    }
    //this is the method for taking input
    void tInput(){
        Scanner s1=new Scanner(System.in);
        System.out.println("start giving input");
        int[] Ar=new int[3];
        for(int i=0;i<3;i++){
            Ar[i]=s1.nextInt();
            
        }
        display(Ar);
    }
    
    //this is the method for displaying array
    void display(int[] Arr) {
        System.out.println("Start of Display");
        for (int trk = 0; trk < Arr.length; trk++) {

            System.out.println(Arr[trk] + " ");
        }
        System.out.println("End of Display");
    }
    
    //linke for char reader
    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
}
