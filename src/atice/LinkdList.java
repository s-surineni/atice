//package atice;

/**
 *
 * @author vinnu
 */
class LinkdList<T>
{
    LinkdList<T> head=null;
    LinkdList<T> next = null;
    LinkdList<T> prev = null;
    T obj;
//    int value;
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

//    void display()
//    {
//	for(LinkdList temp = head ;temp != null ;temp = temp.next )
//	    {
//		System.out.println("value is "+temp.value);
//	    }
//
//    }

   void delete(LinkdList<T> list,LinkdList<T> o)
	{
		if(o.prev!=null)
			o.prev.next = o.next;
		else
			list.head = null;
		if(o.next!=null)
			o.next.prev = o.prev;
	} 

//   void search(LinkdList<T> list, int key)
//	{
//            LinkdList<T> temp;
//		for(temp = list.head; temp!= null && temp.obj.value!=key; temp = temp.next);
//		if(temp!=null)
//                    System.out.println("found");
//	}
}
