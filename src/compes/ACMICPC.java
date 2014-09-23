package compes;

import java.util.Scanner;

class ACMICPC
{
     public static void main(String[] args)
     {
	  ACMICPC a = new ACMICPC();
	  a.begin();
     }

     void begin()
     {
	  Scanner sc = new Scanner(System.in);
	  int pipl = sc.nextInt();
	  int sub = sc.nextInt();
	  char[][] ppl = new char[pipl][sub];
	  for(int i = 0;i<ppl.length;i++)
	  {
	       ppl[i]=sc.next().toCharArray();
	  }
	  int[] pepl=decToBin(ppl,sub);
	  int max = 0;
	  int team=0;
	  for(int i = 0;i<pepl.length;i++)
	  {
	       for(int j = i+1;j<pepl.length;j++)
	       {
		    System.out.println("i now "+pepl[i]);
		    System.out.println("j now "+pepl[j]);
		    int ones = 0;
		    int curr = pepl[i]|pepl[j];
		    System.out.println("sum now "+curr);

		    for(int k = 0;k<sub;k++)
		    {
			 ones = ones+((curr>>k)%2); 
		    }

		    System.out.println("ones now "+ones);
		    if(max<ones)
		    {
			 max = ones;
			 team=0;
		    }
		    if(max==ones)
			 team++;
		    System.out.println("max now "+max);
		    System.out.println("team now "+team);
		    System.out.println();

	       }
	  }
	  System.out.println(max);
	  System.out.println(team);

     }
     int[] decToBin(char[][] ppl,int sub)
     {
	  int[] dec = new int[ppl.length];
	  for(int i = 0;i<ppl.length;i++)
	  {
	       //int binNum = ppl[i];
	       //int rem = 0;
	       int decNum = 0;
	       for(int j=0;j<sub;j++)
	       {
		    //rem = binNum%10;
		    //binNum/=10;
		    decNum+=ppl[i][j]*(Math.pow(2,j));

	       }
	       dec[i]=decNum;
	  }
	  return dec;
     }
}
