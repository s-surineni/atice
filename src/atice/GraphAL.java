package atice;
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
	  createGraph();
     }


     void popGraph ()
     {
	  ver = sc.nextInt();
	  arrL = new ArrayList[ver];
	  for(int i = 0;i<ver;i++)
	  {
	       arrL[i] = new ArrayList();
	       int adj = sc.nextInt();
	       int nextVer;
	       for(int j = adj;j>0;j--)
	       {
		    nextVer = sc.nextInt();
		    nextVer--;
		    System.out.println(nextVer);
		    arrL[i].li.insert(new Vertex(nextVer,i)); 
	       }

	  }
	  //System.out.println("in graph");
	  for(int i=0;i<ver;i++)
	  {
	       //   System.out.println("next");
	       for(LinkdNode<Vertex> lint=arrL[i].li.head ; lint!=null;lint = lint.next)
	       {
		    //	    System.out.println(lint.ele.id);
		    //System.out.println(lint.ele.p.id);
	       }
	  } 
     }
     ArrayList[] createGraph ()
     {
	  System.out.println("Enter name of the file");
	  try
	  {
	       sc = new Scanner(System.in);
	       String filNam = sc.next();
	       sc = new Scanner(new File(filNam));
	  }
	  catch(FileNotFoundException e)
	  {
	       System.out.println("file not found");
	  }
	  ver = sc.nextInt();
	  arrL = new ArrayList[ver];
	  for(int i = 0;i<ver;i++)
	  {
	       arrL[i] = new ArrayList();
	       int adj = sc.nextInt();
	       int nextVer;
	       int verWeigh;
	       for(int j = adj;j>0;j--)
	       {
		    nextVer = sc.nextInt();
		    verWeigh = sc.nextInt();
		    arrL[i].li.insert(new Vertex(nextVer,i,verWeigh)); 
	       }

	  }
	  display(arrL);
	  return arrL;
     }
     void display(ArrayList[] arrL)
     {
	  System.out.println("in graph");
	  for(int i=0;i<ver;i++)
	  {
	       System.out.println("next vertex "+(i));
	       for(LinkdNode<Vertex> lint=arrL[i].li.head ; lint!=null;lint = lint.next)
	       {
		    System.out.print("id "+(lint.ele.id));
		    System.out.println(" wei "+lint.ele.d);
	       }
	  }

     }
}
