import java.util.Scanner;

class Kangaroo
{
     public static void main(String[] args)
     {
          Scanner sc = new Scanner(System.in);
	  long tc = sc.nextLong();
	  for(int i = 0;i<tc;i++)
	  {
	       long st = sc.nextLong();
	       long ed = sc.nextLong();
	       long hop = sc.nextLong();
	       long jumps = 0;
	       long nextmul = (st/hop)+st;
	       if(nextmul<=ed)
	       {
		    jumps++;
	       }
	       jumps+=(ed-nextmul)/hop;
	       System.out.println(jumps);
	  }
     }
}
