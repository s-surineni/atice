class LinkdList<T>
{
    LinkdList<T> head=null;
    LinkdList<T> next = null;
    LinkdList<T> prev = null;
    T obj;
    int value;
    public static void main(String[] args)
    {

    }

    void insert(LinkdList<T> list,T ele)
    {
	LinkdList<T> temp = new LinkdList<T>();
	temp.obj = ele;
	temp.next = list.head;
	if(list.head!=null)
	    {
		list.head.prev = temp;
	    }
	temp.prev = null;
	list.head = temp;
	//display();
    }

    void display()
    {
	for(LinkdList temp = head ;temp != null ;temp = temp.next )
	    {
		System.out.println("value is "+temp.value);
	    }

    }
}
