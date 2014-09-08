//package atice;
import java.io.IOException;
import java.io.BufferedReader;
import java.util.Scanner;
import java.io.InputStreamReader;
import java.io.File;
import java.io.FileNotFoundException;
public class GraphAL {
     private ArrayList[] arrL;
     private int ver;   
     private Scanner sc;
    //     private BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
     public static void main(String[] args)
     {
	  GraphAL gl = new GraphAL();
	  gl.begin();
     }

     void begin()
     {
	  createArrL();
     }

     private void createArrL()
     {
	  System.out.println("Enter the number of vertices in graph");
	  try
	      {
		  sc = new Scanner(new File("graph"));
	      }
	  catch(FileNotFoundException e)
	      {
	      }
	  ver = sc.nextInt();
	  arrL = new ArrayList[ver];
	  popGraph();
     }

     void popGraph ()
     {
	  for(int i = 0;i<ver;i++)
	  {
	      for(int j = sc.nextInt();j>0;j--)
		    {
		    	 arrL[i] = new ArrayList();
			 arrL[i].li.insert(arrL[i].li,sc.nextInt()); 
		    }
	  
	       
	  }
     }
}
