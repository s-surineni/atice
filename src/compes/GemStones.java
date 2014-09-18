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
	  int[] ele = new int[26];
	  for(int i = 0;i<stone.length;i++)
	  {
	       ele[stone[i]-97] = 1;
	  }
	  stones--;
	  for(int i = 0;i<stones;i++)
	  {
	       stone = sc.next().toCharArray();
	       stone = quickSort(stone,0,stone.length-1);
	       stone = remDupli(stone);
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
     char[] quickSort(char[] nos,int st,int end)
     {
         if(st<end)
	  {
	       int indOfP = partition(nos,st,end);
	       quickSort(nos,st,indOfP-1);
	       quickSort(nos,indOfP+1,end);
	  }
	  return nos;
     }

int partition(char[] nos,int st,int end)
     {
	  int pivInd = st-1;
	  for(int i = st;i<= end;i++)
	  {
	       if(nos[i]<=nos[end])
	       {
		    pivInd++;
		    char tmp = nos[pivInd];
		    nos[pivInd] = nos[i];
		    nos[i]=tmp;
	       }
	  }
	  return pivInd;
     }
}
