package atice;

class ListInt
{
    LinkdList<ListInt> listInt;
    int value;
	ListInt(int val)
	{
		value = val;
	}
	ListInt()
	{
	}
    public static void main(String[] args)
    {
	ListInt lI = new ListInt();
	lI.begin();
    }

    void begin()
    {
		listInt = new LinkdList();
		
		for(int i = 0 ; i<10;i++)
		{
			ListInt tmp = new ListInt(i);
			listInt.insert(listInt,tmp);
		}
		display();
		listInt.search(listInt,0);	
    }	
//    void search(LinkdList<ListInt> list, int key)
//	{
//		for(LinkdList<ListInt> temp = list.head; temp!= null && temp.obj.value!=key; temp = temp.next);
//		System.out.println("found");
//	}
	void display()
	{
		System.out.println("in display");
		for(LinkdList<ListInt> tmp = listInt.head;tmp != null ;tmp = tmp.next)
		{
			System.out.println(tmp.obj.value);
		}
	}
}
