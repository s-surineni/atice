//package atice;

/**
 *
 * @author vinnu
 */
class LinkdList<T>
{
    LinkdNode<T> head;
//    int value;
    public static void main(String[] args)
    {

    }
     
    void insert(T el)
    {
	LinkdNode<T> temp = new LinkdNode<T>();
	temp.ele = el;
	temp.next = head;
	if(head!=null)
	    {
		head.prev = temp;
	    }
	temp.prev = null;
	head = temp;
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

   void delete(LinkdList<T> list,LinkdNode<T> o)
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
