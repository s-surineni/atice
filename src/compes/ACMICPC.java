package compes

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
		    int ones = 0;
		    int curr = ppl[i]|ppl[j];
		    for(int k = 0;k<sub;k++)
		    {
			ones = ones+((ppl>>k)%2); 
		    }
		    if(max<ones)
		    {
			 max = ones;
			 team=0;
		    }
		    team++;
	       }
	  }
	  System.out.println(max);
	  System.out.println(team);

     }
     decToBin(int[] ppl,int sub)
     {
	  for(int i = 0;i<sub;i++)
	  {
	       
	  }
     }
}
