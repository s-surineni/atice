class Graph
{
    public static void main(String[] a)
    {
	Graph g = new Graph();
	g.begin();
	System.out.println(-((1<<31)+1));
    }
    void begin()
    {

    }
    void InitSingSource(int len,int src)
    {
	 Vertex v[] = new Vertex[len];
	for(int itr = 0; itr<len;itr++)
	    {
	       
		 v[itr].d=-((1<<31)+1);
	    }
	    v[src].d=0;
    }

    void makeHeap(Vertex[] ver,len)
    {
	 int nonLeaf = (len/2)-1;
	 for(int i = nonLeaf;i>=0;i--)
	 {
	       heapify(ver,i,len);
	 }
    }

    void heapify(Vertex[] ver,int i,int len)
    {
	  int lc = 2*i+1;
	  int rc = 2*i+2;
	  int min=i;
	  if(rc+1<=len && ver[rc].d<ver[i].d)
	  {
	       min=rc;
	  }
	  if(lc+1<= len && ver[lc].d<ver[min].d)
	  {
	       min = lc;
	  }
	  if(min!=i)
	  {
	       int temp = ver[min].d;
	       ver[min].d=ver[i].d;
	       ver[i].d=temp;
	       heapify(ver,min,len);
	  }
	  }


    }

}
