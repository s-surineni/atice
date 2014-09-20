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
	       int st= sc.nextInt();
	       int ed = sc.nextInt();
	       System.out.println(st +" "+ed);
	       int fsq = findFirstSqr(st);
	       //this is for calculating square less or equal to first digit
	       if(j==st)
		    sqrs++;

	       System.out.println("total squares " + sqrs);
	       System.out.println();
	  }
     }

     int findFirstSqr(int st)
     {
	  int dec = 10;//powers of 10 to get digits we consider
	  int dig = 1;//stores total no of digits
	  while((st/dec) >= 1)
	  {
	       dec*=10;
	       dig++;
	  }    //this is to count number of digits
	  System.out.println("digits "+dig);
	  int tp = 0;//gets the power of 10 for getting digits we should consider
	  if(dig%2==0)
	  {
	       tp = dig-2;
	       dig-= 2;//for checking when to exit
	  }
	  else
	  {
	       tp = dig-1;
	       dig--;
	  }
	  tp=dig;
	  System.out.println("ten powr "+tp);
	  tp = (int)Math.pow(10,tp);
	  System.out.println("ten  "+tp);
	  int dtc = st/tp;
	  System.out.println("dig to consider "+dtc);
	  int div = 0;//this stores divisor
	  for(div = 1;div*div<=dtc;div++);
	  div--;
	  int rem = dtc%(div*div);
	  System.out.println("sq of 1st digs "+div);
	  System.out.println("remainder is "+rem);
	  while(dig!=0)
	  {
	       rem = rem *100;
	       int rem2 = st%tp;
	       tp -= 2;
	       dtc = rem + rem2;

	       System.out.println("next dtc "+dtc);
	       dig-=2;
	       tp=dig;
	       System.out.println("ten powr "+tp);
	       tp = (int)Math.pow(10,tp);

	       System.out.println("ten  "+tp);
	       dtc = st/tp;
	       div *=10;
	       if((div+1)<dtc)
	       {
		    tp = tp/10;
		    rem2 = st*10;
		    dtc = rem+rem2;
	       }
	       div *=10;
	       if((div+1)<dtc)

	       for(int j = 1;(div+j)*(j)<=dtc;j++);
	       div--;
	       System.out.println("sq of next digs "+div);
	  }
	  return 0;
     }
}
