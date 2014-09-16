class AllPairsShortPath
{
     JavaL jl = new JavaL();
     int nv ;
     public static void main(String[] a)
     {
	  AllPairsShortPath apsp = new AllPairsShortPath();
	  apsp.begin();
     }

     void begin()
     {
	  int[][] grph = new GraphAM().getGraph();
	  jl.display(grph);
	  nv = grph.length;
	  int[][] done = makeAPSP(grph,grph);
	  jl.display(done);
     }

     int[][] makeAPSP(int[][] L,int[][] W)
     {
	  int max = ((1<<20));
	  System.out.println("max "+max);
	  int ver = L.length;
	  int[][] NL = new int[ver][ver];
	  for(int i = 0;i<ver;i++)
	  {
	       for(int j = 0;j<ver;j++)
	       {
		    NL[i][j]=max;
		    for(int k = 0;k<ver;k++)
		    {
			 NL[i][j] = min(NL[i][j],L[i][k]+W[k][j]);
		    }
	       }
	  }
	  if(nv == 1)
	  {
	       jl.display(NL);
	       return NL;
	  }
	  else
	  {
	       jl.display(NL);
	       nv--;
	       NL = makeAPSP(NL,W);
	       return NL;
	  }
     }
     int[][] AllPairsShortLen(int[][] L,int[][] W)
     {
	  int max = ((1<<20));
	  System.out.println("max "+max);
	  int ver = L.length;
	  int[][] NL = new int[ver][ver];
	  for(int i = 0;i<ver;i++)
	  {
	       for(int j = 0;j<ver;j++)
	       {
		    NL[i][j]=max;
		    for(int k = 0;k<ver;k++)
		    {
			 NL[i][j] = min(NL[i][j],L[i][k]+W[k][j]);
		    }
	       }
	  }
	  return NL;
     }
     int min(int a,int b)
     {
	  if(a>b)
	       return b;

	  return a;
     }
}
