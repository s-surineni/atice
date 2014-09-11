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

	void makeHeap(Vertex[] ver,int len)
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
			int tempid = ver[min].id;
			ver[min].d=ver[i].d;
			ver[min].id=ver[i].id;
			ver[i].d=temp;
			ver[i].id=tempid;
			heapify(ver,min,len);
		}
	}

	void relax(Vertex[] ver,int to,int par,int dist,int dist2)
	{
	       if(ver[to].d>dist+dist2)
	       {
		    ver[to].d = dist+dist2;
		    ver[to].p = par;
	       }
	}
}
