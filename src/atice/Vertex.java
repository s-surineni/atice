package atice;
class Vertex
{

     int p;
     int d;
     int id;
     Vertex(int idf,int par,int dis)
     {
	  id=idf;
	  p=par;
	  d=dis;
     }
     Vertex(int idf,int par)
     {
	  id = idf;
	  p = par;
     }
     Vertex()
     {
     }

}
