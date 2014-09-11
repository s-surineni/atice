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
          int len = ver.length;
          Graph g = new Graph();
          System.out.println("enter the source you wanted");
          int src = sc.nextInt();
          ver = g.initSingSource(ver,src);
          for(int i = 0;i<len;i++)
          {
               int u = 
          }
     }
}
