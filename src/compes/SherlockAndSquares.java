package compes;
import java.util.Scanner;

class SherlockAndSquares
{
     public static void main(String[] args)
     {
	  SherlockAndSquares saq = new SherlockAndSquares();
	  saq.begin();
     }

     void begin()
     {
	  Scanner sc = new Scanner(System.in);
	  int tc = sc.nextInt();
	  for(int i = 0;i<tc;i++)
	  {
	       int st= sc.nextInt();
	       int ed = sc.nextInt();
	       System.out.println(st +" "+ed);
	       int dec = 10;
	       int dig = 1;
	       while(st/dec > 1)
	       {
		    dec*=10;
		    dig++;
	       }
	  }
     }
}
