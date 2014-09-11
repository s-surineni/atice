import java.util.Scanner;

class Dijkstra
{
     public static void main(String[] args)
     {
          Dijkstra dk = new Dijkstra();
          dk.begin();
     }

     void begin()
     {
          Scanner sc = new Scanner(System.in);
          GraphAL grph =new GraphAL();
          ArrayList[] al= grph.popWeighGraph();
          Vertex[] ver = new Vertex[al.length];
          int glen = ver.length;
	  int hlen = glen;
          Graph g = new Graph();
          System.out.println("enter the source you wanted");
          int src = sc.nextInt();
          g.initSingSource(ver,src);
	  g.makeHeap(ver,glen);
          for(int i = 0;i<glen;i++)
          {
	       //ver = g.
               int u = ver[0].id;//gives the one with shortest dist form last vertex
	       int dist = ver[i].d;
	       for(LinkdNode<Vertex> tmp = al[u].li.head;tmp!=null;tmp = tmp.next)
	       {
		    display(ver);
		    g.relax(ver,tmp.ele.id,u,dist,tmp.ele.d);
		    display(ver);
	       }
	       hlen--;
	       Vertex tmp = ver[0];
	       ver[0]=ver[hlen];
	       ver[hlen]=tmp;
	       g.heapify(ver,0,hlen);
          }
	  display(ver);
     }

     void display(Vertex[] Arr) {
	  System.out.println("Start of Display");
	  for (int trk = 0; trk < Arr.length; trk++) {

	       System.out.println(Arr[trk].id+1 + " "+Arr[trk].d);
	  }
	  System.out.println("End of Display");
     }
}
