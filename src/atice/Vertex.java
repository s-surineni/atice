class Vertex
{

    Vertex p;
    int d;
    int id;
    Vertex(int idf,Vertex par,int dis)
    {
	 id=idf;
	p=par;
	d=dis;
    }
    Vertex(int idf,Vertex par)
    {
	id = idf;
	p = par;
    }
    Vertex()
    {
    }

}
