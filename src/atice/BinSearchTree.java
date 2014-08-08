import java.util.Scanner;
class BinSearchTree
{
	BinSearchTree bst2;
	IntNode root = null;
	Scanner sc= new Scanner(System.in);
	Scanner isc = new Scanner(System.in);
	int key;

	public static void main(String[] args)
	{
		BinSearchTree bst = new BinSearchTree();
		bst.begin();
	}

	void begin()
	{
		bst2 = new BinSearchTree();
		char uIn='y';
		do
		{
			switch (uIn)
			{
				case 'i':
				System.out.println("Enter the value you want to insert");
				key = isc.nextInt();
				insert(bst2,new IntNode(key));
					break;
				case 's':
					System.out.println("Enter value to search for");
					key = isc.nextInt();
					IntNode serch=search(root,key);
					if(serch != null)
						System.out.println("found");
					else
						System.out.println("not found");
					break;
				case 'm':
					IntNode min = minm(root);
					if(min != null)
						System.out.println("minimum is "+min.key);
					else
						System.out.println("the tree has no leaves");
					break;
				case 'M':	
					IntNode max = maxm(root);
					if(max != null)
						System.out.println("maximum is "+max.key);
					else
						System.out.println("the tree has no leaves");
					break;	
				case 'u':	
					System.out.println("Enter key of ele of which you want to find the successor of");
					key = isc.nextInt();
					IntNode nod = search(root,key);
					IntNode scr = success(nod);
					if(scr != null)
						System.out.println("successor is "+scr.key);
					else
						System.out.println("this is the largest element");
					break;	
				case 'p':	
					System.out.println("Enter key of ele of which you want to find the predecessor of");
					key = isc.nextInt();
					nod = search(root,key);
					scr = success(nod);
					if(scr != null)
						System.out.println("predecessor is "+scr.key);
					else
						System.out.println("this is the smallest element");
					break;	
			}
			System.out.println("Insert i");
			System.out.println("search s");
			System.out.println("minimum m");
			System.out.println("maximum M");
			System.out.println("successor u");
			System.out.println("predecessor p");
			System.out.println("Exit x");
				

		}while((uIn = sc.next().charAt(0))!= 'x');
	}
	void insert(BinSearchTree tree,IntNode n)
	{
		Node temp1 = null;
		Node temp2 = root;
		
		while(temp2 != null)
		{
			temp1 = temp2;
			if(((IntNode)temp2).key< n.key)
				temp2 = temp2.rChild;
			else
				temp2 = temp2.lChild;
		}
		if(temp1 == null)
			root = n;
		else
		{
			n.parent = temp1;
			if(((IntNode)temp1).key < n.key)
			{
				System.out.println("rchild");
				temp1.rChild = n;
			}
			else
			{
				System.out.println("lchild");
				temp1.lChild = n;
			}
		}
		System.out.println("Inoder Tree Walk");
		inTreeWalk(root);
		
	}

	void inTreeWalk(Node temp)
	{	
		
		if(temp !=null)
		{
			inTreeWalk(((IntNode)temp).lChild);
			System.out.println(((IntNode)temp).key);
			inTreeWalk(temp.rChild);
		}
	}

	IntNode search(Node tmpRt,int ky)
	{
		if(tmpRt == null || ((IntNode)tmpRt).key == ky )
		{
			return (IntNode)tmpRt;
		}
		if(((IntNode)tmpRt).key <= ky)
		{
			return search(tmpRt.rChild,ky);
		}
		else
			return search(tmpRt.lChild,ky);
	}	

	IntNode minm(Node tmpRt)
	{
		while(((IntNode)tmpRt).lChild != null)
			tmpRt = tmpRt.lChild;
		return (IntNode)tmpRt;
	}

	IntNode maxm(Node tmpRt)
	{
		while(((IntNode)tmpRt).rChild != null)
			tmpRt = tmpRt.rChild;
		return (IntNode)tmpRt;
	}
	
	IntNode success(Node sR)
	{
		if(sR.lChild != null)
			return maxm(sR.lChild);
		Node y = sR.parent;
		while(y != null && sR == y.lChild)
		{
			sR = y;
			y = sR.parent;
		}
		return (IntNode)y;
	}

	IntNode predec(Node sR)
	{
		if(sR.rChild != null)
			return minm(sR.rChild);
		Node y = sR.parent;
		while(y != null && sR == y.rChild)
		{
			sR = y;
			y = sR.parent;
		}
		return (IntNode)y;
	}
	
	void transplant(Node to,Node frm)
	{
		if(to.parent == null)
			bst2.root = frm;
		else
		{
			if(to.parent.lChild == to)
			{
				to.parent.lChild = frm;
			}

			else
				to.parent.rChild = frm;
		}
		if(frm != null)
		{
			frm.parent = to.parent;
		}
	}











}
