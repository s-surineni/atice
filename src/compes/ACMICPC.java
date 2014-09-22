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
	  int[] ppl = new int[sc.nextInt()];
	  int sub = sc.nextInt();
	  for(int i = 0;i<ppl.length;i++)
	  {
	       ppl[i]=sc.nextInt();
	  }
	  decToBin(ppl,sub);
	  int max = 0;
	  int team=0;
	  for(int i = 0;i<ppl.length;i++)
	  {
	       for(int j = i+1;j<ppl.length;j++)
	       {
		    //System.out.println("i now "+ppl[i]);
		    //System.out.println("j now "+ppl[j]);
		    int ones = 0;
		    int curr = ppl[i]|ppl[j];
		    //System.out.println("sum now "+curr);

		    for(int k = 0;k<sub;k++)
		    {
			 ones = ones+((curr>>k)%2); 
		    }

		    //System.out.println("ones now "+ones);
		    if(max<ones)
		    {
			 max = ones;
			 team=0;
		    }
		    if(max==ones)
			 team++;
		    //System.out.println("max now "+max);
		    //System.out.println("team now "+team);
		    //System.out.println();

	       }
	  }
	  System.out.println(max);
	  System.out.println(team);

     }
     void decToBin(int[] ppl,int sub)
     {
	  for(int i = 0;i<ppl.length;i++)
	  {
	       int binNum = ppl[i];
	       int rem = 0;
	       int decNum = 0;
	       for(int j=0;j<sub;j++)
	       {
		    rem = binNum%10;
		    binNum/=10;
		    decNum+=rem*(Math.pow(2,j));

	       }
	       ppl[i]=decNum;
	  }
     }
}
