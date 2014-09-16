//https://www.hackerrank.com/challenges/gem-stones
import java.util.Scanner;
class GemStones
{
     public static void main(String[] a)
     {
	  GemStones gs = new GemStones();
	  gs.begin();
     }

     void begin()
     {
	  Scanner sc = new Scanner(System.in);
	  int stones = sc.nextInt();
	  int gems = stones;
	  char[] stone = sc.next().toCharArray();
	  char[] ele = new char[26];
	  for(int i = 0;i<stone.length;i++)
	  {
	       ele[stone[i]-97] = 1;
	  }
	  stones--;
	  for(int i = 0;i<stones;i++)
	  {
	       stone = sc.next().toCharArray();
	       for(int j = 0;j<stone.length;j++)
	       {
		    ele[stone[j]-97]++;
	       }
	  }
	  int j = 0;
	  for(int i = 0;i<ele.length;i++)
	  {
	      if(ele[i]==gems)
		   j++;
	  }
	  System.out.println(j);

     }
}
