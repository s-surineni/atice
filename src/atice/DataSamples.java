//samples of data for programs
import java.util.Random;

public class DataSamples
{
	int[] randomArr = {1,0,2,9,3,8,4,7,5,6};
	int[] getRandomArr(int uLimit)
	{
		int[] arrToRet	= new int[uLimit];
		Random rn = new Random();
		for(int i =0;i<uLimit;i++)
		{
			arrToRet[i] = rn.nextInt(uLimit);
		}
		return arrToRet;
	}

}
