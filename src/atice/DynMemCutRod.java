import java.util.Scanner;

class DynMemCutRod
{

     int prof[] = {0,1,5,8,9,10,17,17,20,24,30};
     int rev[];
    public static void main(String[] args)
    {
	 DynMemCutRod dm = new DynMemCutRod();
	 dm.begin();
    
    }

     void begin()
     {
	  Scanner sc = new Scanner(System.in);
	  System.out.println("Enter the size of the rod");
	  int siz = sc.nextInt();
	  System.out.println("The max profit of "+siz+" is "+memCutRod(siz));
     }
    int  memCutRod(int siz)
    {
	 rev = new int[siz+1]; 
	  rev[0] = 0;
	  int neg = 1 << 31;
	 
	 for(int i = 1; i<=siz; i++)
	 {
	      rev[i] = neg;
	 }

	 return memCutRodAux(siz,rev);
    }

    int memCutRodAux(int siz,int[] rev)
    {

	  if(rev[siz] >= 0)
	  {
	       return rev[siz];
	  }
	  
	  int q = 1 << 31;

	  for(int i = 1; i<=siz; i++)
	  {
	       q = max(q,prof[i]+memCutRodAux(siz - i,rev));
	       
	  }
	  rev[siz] = q;

	  return q;
    }

    int max(int a,int b)
    {
	 if(a>b)
	      return a;
         else
	      return b;
    }


} 
