package compes;
import java.util.Scanner;

class VimDig
{
     public static void main(String[] args)
     {
	  VimDig vd = new VimDig();
	  vd.begin();
     }

     void begin()
     {
	  Scanner sc = new Scanner(System.in);
	  int tc = sc.nextInt();
	  for(int i=0;i<tc;i++)
	  {
	       int rem;
	       int num =rem= sc.nextInt();
	       int ten = 10;
	       int dig = 1;
	       for(;(int)Math.pow(10,dig)<=num;dig++);
	       int n=0;
	       for(;dig>0;dig--)
	       {
		    int ds=(int)Math.pow(10,dig-1);

		    int q =rem/ds;
		    try
		    {
			 if(num%q==0)
			 {
			      n++;
			 }
		    }
		    catch(ArithmeticException a)
		    {

		    }
		    rem = rem%ds;
	       }
	       System.out.println(n);
	  }
     }
}
