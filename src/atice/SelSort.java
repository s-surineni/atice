package atice;

//selection sort 2.2-2 pg 29
public class SelSort
{
	public static void main(String[] args)
	{
		int Arr[] = new DataSamples().randomArr;
		new SelSort().selSort(Arr);
	}

	private void selSort(int A[])
	{
		for(int i = 0;i<A.length-1;i++)
		{
			int smallest = A[i];
			int sind = i;	
			for(int j = i;j<A.length;j++)
			{
				if(smallest>A[j])
				{
					smallest = A[j];
					sind = j;
					
				}
			}
			int temp = A[i];
			A[i]=A[sind];
			A[sind]=temp;
		}
		new JavaL().display(A);						
	}
}
