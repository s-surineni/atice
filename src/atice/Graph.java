class Graph
{
    public static void main(String[] a)
    {
	Graph g = new Graph();
	g.begin();
    }
    void begin()
    {

    }
    void InitSingSource(ArrayList[] al,int src)
    {
	for(int itr = 0; itr<al.length;itr++)
	    {
		al[itr].li.obj.p =null;
		al[itr].li.obj.d=1<<31;
	    }
	al[src].li.obj.p=null;
	al[src].li.obj.d=0;
    }
}
