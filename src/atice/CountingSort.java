package atice;

import java.util.Scanner;

class CountingSort
{
     public static void main(String[] a)
     {
	  CountingSort cs = new CountingSort();
	  cs.begin();
     }

     void begin()
     {
	  Scanner sc = new Scanner(System.in);
	  System.out.println("Enter the number of elements");
	  int num = sc.nextInt();
	  int ele[] = new int[num];
	  int done[] = new int[num];
	  for(int i = 0;i<num;i++)
	  {
	       ele[i] = sc.nextInt();
	  }
	  int stor[] = new int[5+1];
	  for(int i = 0;i<num;i++)
	  {
	       stor[ele[i]] = stor[ele[i]]+1;
	  }
	  for(int i = 1;i<stor.length;i++)
	  {
	       stor[i] = stor[i]+stor[i-1];
	  }
	  new JavaL().display(stor);
	  for(int i = num-1;i>=0;i--)
	  {
	       done[stor[ele[i]]-1] = ele[i];
	       stor[ele[i]]--;
	  }
	  new JavaL().display(done);
	  
	  
     }
}
