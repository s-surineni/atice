//https://www.hackerrank.com/challenges/gem-stones
package compes;
import atice.JavaL;
import atice.QuickSort;
import java.util.Scanner;
class GemStones
{
     JavaL jl = new JavaL();
     public static void main(String[] a)
     {
	  GemStones gs = new GemStones();
	  gs.begin();
     }

     void begin()
     {
	  Scanner sc = new Scanner(System.in);
	  QuickSort qs = new QuickSort();
	  int stones = sc.nextInt();
	  int gems = stones;
	  char[] stone = sc.next().toCharArray();
	  int[] ele = new int[9];
	  for(int i = 0;i<stone.length;i++)
	  {
	       ele[stone[i]-97] = 1;
	  }
	  display(ele);
	  stones--;
	  for(int i = 0;i<stones;i++)
	  {
	       stone = sc.next().toCharArray();
	       stone = qs.quickSort(stone,0,stone.length-1);
	       display(stone);
	       System.out.println();
	       stone = remDupli(stone);
	       display(stone);
	       System.out.println();
	       for(int j = 0;j<stone.length;j++)
	       {
		    ele[stone[j]-97]++;
	       }
	       display(ele);
	  }
	  int j = 0;
	  for(int i = 0;i<ele.length;i++)
	  {
	      if(ele[i]==gems)
		   j++;
	  }
	  System.out.println(j);

     }

     char[] remDupli(char[] c)
     {
	  int siz = c.length;
	  int ns = siz;
	  for(int i = 0;i<siz-1;i++)
	  {
	       if(c[i]==c[i+1])
	       {
		    ns--;
		    c[i] = '\0';
	       }
	  }
	  char[] s = new char[ns];
	  for(int i = 0,j=0;i<siz;i++)
	  {
	       if(c[i]!='\0')
	       {
		    s[j]=c[i];
		    j++;
	       }
	  }
	  return s;
	  
     }
     void display(char[] Arr) {
	  for (int trk = 0; trk < Arr.length; trk++) {

	       System.out.println(Arr[trk] + " ");
	  }
	  System.out.println();
     }
     void display(int[] Arr) {
	  for (int trk = 0; trk < Arr.length; trk++) {

	       System.out.println(Arr[trk] + " ");
	  }
	  System.out.println();
     }
}
