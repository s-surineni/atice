class ListInt
{
    LinkdList<Integer> listInt;
    int value;
    public static void main(String[] args)
    {
	ListInt lI = new ListInt();
	lI.begin();
    }

    void begin()
    {
		listInt = new LinkdList<>();
		listInt.insert(listInt,1);
		display();
		
    }
	void display()
	{
		System.out.println("in display");
		for(LinkdList<Integer> tmp = listInt.head;tmp != null ;tmp = tmp.next)
		{
			System.out.println(tmp.obj.value);
		}
	}
}
