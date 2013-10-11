/*this file implements the tree
 * 
 * 
 */
package atice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 *
 * @author vinnu
 */
public class Tree {
    
    public static void main(String[] args) throws IOException{
        int[] Atre=new int[100];
        System.out.println("please enter the values in a tree");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter x to exit after entering the numbers");
        char ip=(char)br.read();
        for(int trk=0;ip!='x';trk++){
            Atre[trk]=(int)ip;
            System.out.println("the value entered is " + ip);
            ip=(char)br.read();
        }

    }
    
}
