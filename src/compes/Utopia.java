package compes;
import java.util.Scanner;
class Utopia
{
     public static void main(String[] a)
     {
	  Scanner sc = new Scanner(System.in);
	  int tc = sc.nextInt();
	  for(int i = 0;i<tc;i++)
	  {
	       int cycs = sc.nextInt();
	       int h = 1;
	       for(int j = 1;j<=cycs;j++)
	       {
		    if(j%2==1)
			 h*=2;
		    else
			 h+=1;
	       }
	       System.out.println(h);
	  }
     }

}
