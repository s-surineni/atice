// prob 2.1-4 pg 23
public class AddBin
{
	static JavaL jl;	
	public static void main(String[] args)
	{	jl = new JavaL();
		AddBin ab = new AddBin();
		DataSamples ds = new DataSamples();
		int A[] = ds.getRandomArr(10);
		int B[] = ds.getRandomArr(10);
		System.out.println("The array A");
		jl.display(A);
		System.out.println("The array B");
		jl.display(B);
		ab.addAB(A,B);
	}

	private void addAB(int[] A,int[] B)
	{
		for(int i = 0; i<A.length; i++)
		{
			A[i] = A[i] + B[i];
		}
		System.out.println("sum of a and b");
		jl.display(A);
		binarize(A);
	}
	private void binarize(int[] sum)
	{
		for(int i = 0; i<sum.length;i++)
		{	int bin;
			int p=0;
			for(bin=0;sum[i]!=0; sum[i]/=2,p++)
			{
				bin=(int)((bin)+(sum[i]%2)*Math.pow(10,p));	
			}
			sum[i] = bin;
		}
		System.out.println("the binary values");
		jl.display(sum);
	}
}
