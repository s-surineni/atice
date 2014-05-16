// prob 2.1-4 pg 23
public class AddBin
{
	public static void main(String[] args)
	{	
		AddBin ab = new AddBin();
		DataSamples ds = new DataSamples();
		int A[] = ds.getRandomArr(10);
		int B[] = ds.getRandomArr(10);
		ab.addAB(A,B);
	}

	private void addAB(int[] A,int[] B)
	{
		for(int i = 0; i<A.length; i++)
		{
			A[i] = A[i] + B[i];
		}
		binarize(A);
	}
	
}
