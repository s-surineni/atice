//this program is to use insertion sort
package atice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 *
 * @author vinnu
 */
public class isort {
    public static void main(String[] args) throws IOException {
        isort is=new isort();
        is.start();
        
    }
    
    void start() throws IOException{
        System.out.println("how many number of elements do you want to sort");
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int size=br.read()-48;
        
        int[] Sore=new int[size];
        System.out.println("size "+size);
        System.out.println("please enter the numbers you want to sort");
        System.out.println("don't forget to press enter after entering each element");
        for(int trk=0;trk<size;trk++){
            
            Sore[trk]=br.read()-48;
        System.out.println("see " +trk);
            System.out.println("sore value "+Sore[trk]);
            
        }
        System.out.println("the values you have entered is ");
        for(int trk1=0;trk1<size;trk1++){
            System.out.println(Sore[0]+" ");
            
        }
    }
    
    
}
