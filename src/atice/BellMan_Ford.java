package atice;

class BellMan_Ford
{
     public static void main(String[] a)
     {
	  BellMan_Ford bf = new BellMan_Ford();
	  bf.begin();
     }

     void begin()
     {
	  GraphAL grph = new GraphAL();
	  ArrayList[] gph = grph.createGraph();
	  int vers = gph.length;
	  Vertex v[] = new Vertex[vers];
	  Graph gm = new Graph();
	  gm.initSingSource(v,0);
	  for(int i = 0;i<vers-1;i++)
	  {
	       for(int j = 0;j<vers;j++)
	       {
		    for(LinkdNode<Vertex> tr = gph[j].li.head;tr != null;tr = tr.next)
		    {
			 gm.relax(v[j],v[tr.ele.id],tr.ele.d);
		    }
	       }
	       gm.display(v);
	  }
	  gm.display(v);
	  for(int j = 0;j<vers;j++)
	  {
	       for(LinkdNode<Vertex> tr = gph[j].li.head;tr != null;tr = tr.next)
	       {
		    if(v[tr.ele.id].d>v[j].d+tr.ele.d)
			 System.out.println("negative cycle");
	       }
	  }
     }
}
