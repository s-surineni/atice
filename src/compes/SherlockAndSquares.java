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
	  int j = 0;
	  for(int i = 0;i<tc;i++)
	  {
	       int sqrs = 0;
	       int totsqrs = 0;
	       int st= sc.nextInt();
	       int ed = sc.nextInt();
	       System.out.println(st +" "+ed);
	       int dec = 10;//powers of 10 to get digits we consider
	       int dig = 1;//stores total no of digits
	       while((st/dec) >= 1)
	       {
		    dec*=10;
		    dig++;
	       }    //this is to count number of digits
	       if(dig==1)
	       {
		    sqrs = 1;
		    for( ; sqrs*sqrs<=st;sqrs++);
		    sqrs--;
		    System.out.println("first root  "+sqrs);

	       }
	       else
	       {
		    if(dig%2==1)
		    {
			 sqrs = (int)Math.pow(10,(dig/2));
			 System.out.println("Start point "+sqrs);
			 for( ; sqrs*sqrs <= st;sqrs++);
			 sqrs--;
			 System.out.println("first root  "+sqrs);


		    }
		    else
		    {
			 sqrs = (int)Math.pow(10,(dig/2));
			 sqrs--;
			 System.out.println("Start point "+sqrs);
			 for( ; sqrs*sqrs > st;sqrs--);
			 System.out.println("first root "+sqrs);

		    }


	       }
	       if(sqrs*sqrs == st)
	       {
		    totsqrs++;
	       }
	       sqrs++;
	       System.out.println("next sq "+(sqrs*sqrs));
	       for( ; sqrs*sqrs <= ed; sqrs++)
	       {
		    totsqrs++;
	       }
	       System.out.println(totsqrs);

	  }
     }
}

