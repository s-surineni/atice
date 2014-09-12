class Graph
{
     Dijkstra dk = new Dijkstra();
     public static void main(String[] a)
     {
	  Graph g = new Graph();
	  g.begin();
	  System.out.println(-((1<<31)+1));
     }
     void begin()
     {

     }
     void initSingSource(Vertex v[],int src)
     {
	  src--;
	  int len = v.length;
	  for(int itr = 0; itr<len;itr++)
	  {
	       v[itr] = new Vertex(itr,0,-((1<<31)+1));
	  }
	  v[src].d=0;
     }

     void makeHeap(Vertex[] ver,int[] locs,int len)
     {
	  int nonLeaf = (len/2)-1;
	  for(int i = nonLeaf;i>=0;i--)
	  {
	       heapify(ver,locs,i,len);
	  }
     }

     void heapify(Vertex[] ver,int[] locs,int i,int len)
     {
	  int lc = 2*i+1;
	  int rc = 2*i+2;
	  int min=i;
	  if(rc<len && ver[rc].d<ver[i].d)
	  {
	       min=rc;
	  }
	  if(lc< len && ver[lc].d<ver[min].d)
	  {
	       min = lc;
	  }
	  if(min!=i)
	  {
	       System.out.println("in heap");
	       System.out.println("vers");
	       dk.display(ver);
	       System.out.println("locs");
	       dk.display(locs);
	       System.out.println(" min "+(min+1)+" minid "+(ver[min].id+1)+" i "+(i+1)+" iid "+(ver[i].id+1));
	       Vertex temp = ver[min];
	       locs[ver[min].id]=i;
	       locs[ver[i].id]=min;
	       ver[min]=ver[i];
	       ver[i]=temp;

	       //new Dijkstra().display(ver);
	       heapify(ver,locs,min,len);
	  }
     }

     void relax(Vertex[] ver,int to,int par,int dist,int dist2)
     {
	  System.out.println("from "+(par+1));
	  System.out.println("to "+(ver[to].id+1));
	  int totaldist = dist+dist2; 
	  System.out.println("dist "+totaldist);
	  System.out.println("pre dist "+ver[to].d);
	  if(ver[to].d>totaldist)
	  {
	       ver[to].d = totaldist;
	       System.out.println("now dist "+ver[to].d);

	       ver[to].p = par;
	  }
     }
}
