package atice;

import java.io.InputStreamReader;
import java.util.Scanner;

class JavaL {

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
        //display(Ar);
    }
    
     //this is the method for displaying array
     void display(char[] Arr) {
	  for (int trk = 0; trk < Arr.length; trk++) {

	       System.out.println(Arr[trk] + " ");
	  }
     }

     void display(int[] Arr) {
	  for (int trk = 0; trk < Arr.length; trk++) {

	       System.out.println(Arr[trk] + " ");
	  }
     }

     void display(int[][] Arr) {
	  System.out.println("Start of Display");
	  int rc = Arr.length;
	  int cc = Arr[0].length;
	  for (int trk1 = 0; trk1 < rc; trk1++) {
	       for (int trk = 0; trk < cc; trk++) {

		    System.out.print(Arr[trk1][trk] + " ");
	       }
	       System.out.println();
	  }

	  System.out.println("End of Display");
     }

}
