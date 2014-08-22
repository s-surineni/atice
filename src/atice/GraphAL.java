//package atice;
import java.io.IOException;
import java.io.BufferedReader;
import java.util.Scanner;
import java.io.InputStreamReader;

public class GraphAL {
     private ArrayList[] arrL;
     private int ver;   
     private Scanner sc;
     private BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
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
	  sc = new Scanner(System.in);
	  try
	  {
	       ver = br.read();
	  }
	  catch(IOException e)
	  {

	  }
	  arrL = new ArrayList[ver];
	  popGraph();
     }

     void popGraph ()
     {
	  for(int i = 0;i<ver;i++)
	  {
	       System.out.println("Enter vertices adjacent to vertes "+
		    i+1);
	       System.out.println("press d when done");
	       try{
		    int adjver = br.read();
		    System.out.println((char)adjver);
		    while( ((char)adjver) != 'd')
		    {
		    	 arrL[i] = new ArrayList();
			 arrL[i].li.insert(arrL[i].li,adjver); 
		    }
	       }
	       catch(IOException e)
	       {
	       }
	  }
     }
}
