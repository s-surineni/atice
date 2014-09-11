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
	  int locs[] = new int[glen];
	  int hlen = glen;
          Graph g = new Graph();
          System.out.println("enter the source you wanted");
          int src = sc.nextInt();
          g.initSingSource(ver,src);
          System.out.println("after ininting");
	  display(ver);
	  g.makeHeap(ver,glen);
          for(int i = 0;i<glen;i++)
          {
	       //ver = g.
               int u = ver[0].id;//gives the one with shortest dist form last vertex
	       int dist = ver[0].d;
	       System.out.println("before relaxing");
	       display(ver);
	       for(LinkdNode<Vertex> tmp = al[u].li.head;tmp!=null;tmp = tmp.next)
	       {    
		    g.relax(ver,tmp.ele.id,u,dist,tmp.ele.d);
	       }
	       System.out.println("after relaxing");
	       display(ver);
	       hlen--;
	       Vertex tmp = ver[0];
	       ver[0]=ver[hlen];
	       ver[hlen]=tmp;
	       g.makeHeap(ver,hlen);
	       System.out.println("after heapify");
	       display(ver);
          }
	  display(ver);
     }

     void display(Vertex[] Arr) {
	  for (int trk = 0; trk < Arr.length; trk++) {

	       System.out.println(Arr[trk].id+1 + " "+Arr[trk].d);
	  }
     }
}
