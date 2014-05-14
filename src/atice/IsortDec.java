public class IsortDec
{
	public static void main(String[] args)
	{
		int Arr[]={1,0,2,9,3,8,4,7,5,6};
		for(int i = 1; i< 10; i++)
		{
			int j = i-1;
			int key = Arr[i];
			for( ; j>= 0 && key > Arr[j];j--)
			{
				Arr[j+1] = Arr[j];
			}
		Arr[j+1] = key;  
		} 
		for(int j = 0;j<10;j++)
		{
			System.out.println(Arr[j]+" ");
		}
	}
}
