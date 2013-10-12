/*this file implements the tree
 * 
 * 
 */
package atice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

/**
 *
 * @author vinnu
 */
public class Tree {
    
    public static void main(String[] args) throws IOException {
        Tree tt=new Tree();
        tt.tInput();

    }
    void tInput() throws IOException{
        System.out.println("enter the number of elements you want in tree");
        Scanner s1=new Scanner(System.in);
        char ip=(s1.next()).charAt(0);
        int[] Atre=new int[ip];
        
        System.out.println("please enter the values in a tree");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter x to exit after entering the numbers");
        ip=(s1.next()).charAt(0);
        for(int trk=0;trk<Atre.length;trk++){
            Atre[trk]=ip-48;
            System.out.println("the value entered is " + ip);
            ip=(s1.next()).charAt(0);
            br.mark(trk);
            br.reset();
        }
        Display(Atre);
        
    }
    void Display(int[] Arr){
        for(int trk=0;trk<Arr.length;trk++){
         
         System.out.println(Arr[trk]+ " ");
        }
    }
    
}
