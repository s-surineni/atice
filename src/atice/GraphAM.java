import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

class GraphAM
{
     JavaL jl = new JavaL();
     public static void main(String[] a)
     {
	  GraphAM gam = new GraphAM();
	  //gam.begin();
     }

     int[][] getGraph()
     {
	  System.out.println("Enter the name of the file");
	  Scanner sc = new Scanner(System.in);
	  File f = new File(sc.next());
	  try
	  {
	       sc = new Scanner(f);
	  }
	  catch(FileNotFoundException e)
	  {

	  }
	  int verts = sc.nextInt();
	  int[][] AdjMat = new int[verts][verts];
	  
	  int max = ((1<<20));
	  for(int i = 0;i<verts;i++)
	  {

	       for(int j = 0;j<verts;j++)
	       {
		   AdjMat[i][j]= max; 
	       }
	  }
	  for(int j = 0;j<verts;j++)
	  {
	       AdjMat[j][j]= 0; 
	  }

	  for(int i = 0;i<verts;i++)
	  {
	       for(int j = sc.nextInt();j>0;j--)
	       {
		    int col = sc.nextInt();
		    AdjMat[i][col] = sc.nextInt();
	       }
	  }
	  //jl.display(AdjMat);
	  return AdjMat;
     }
}
