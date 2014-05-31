package atice;

//pg 22 cormen 2.1-3
public class LinSearch
{
	public static void main(String[] args)
	{
		
		DataSamples ds = new DataSamples();
		JavaL jl = new JavaL();
		System.out.println("element has to be searched in");
		int[] Arr = ds.getRandomArr(10);
		jl.display(Arr);
		LinSearch ls = new LinSearch();
		ls.lSearch(Arr,2);
	}
	
	protected void lSearch(int[] A,int val)
	{
		int i = 0;
		for( ;i<A.length && val!= A[i] ; i++);
		if( i == A.length)
		{
			System.out.println("Element not found");
		}	
		else
			System.out.println(i+1);
	}
}
