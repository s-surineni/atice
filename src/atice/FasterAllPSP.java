package atice;
import java.util.Scanner;

class FasterAllPSP
{
     JavaL jl = new JavaL();
     public static void main(String ar[])
     {
	  FasterAllPSP fast = new FasterAllPSP();
	  fast.begin();
     }

     void begin()
     {
	  int[][] grph = new GraphAM().getGraph();
	  fastAPSP(grph);
     }

     int[][] fastAPSP(int[][] W)
     {
	  AllPairsShortPath apsp = new AllPairsShortPath();
	  int vers = W.length;
	  int reps = 1;
	  for(int p2 = 2 ; p2 < vers;p2*=2,reps++);
	  for(int i = 0;i<reps;i++)
	  {
	       W = apsp.AllPairsShortLen(W,W);
	  }
	  jl.display(W);
	  return W;
     }
}
