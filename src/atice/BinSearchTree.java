class BinSearchTree
{
	IntNode root = null;

	void insert(BinSearchTree tree,IntNode n)
	{
		Node temp1 = null;
		Node temp2 = root;
		
		while(temp2 != null)
		{
			temp1 = temp2;
			if(((IntNode)temp2).key>=	n.key)
				temp2 = temp2.rChild;
			else
				temp2 = temp2.lChild;
		}
		if(temp1 == null)
			root = n;
		else
			n.parent = temp1;
		if(((IntNode)temp1).key >= n.key)
			temp1.rChild = n;
		else
			temp1.lChild = n;
	}

}
