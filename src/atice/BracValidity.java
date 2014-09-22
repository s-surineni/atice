package atice;

import java.util.Scanner;

class BracValidity
{
     public static void main(String[] a)
     {
	  BracValidity bv = new BracValidity();
	  bv.begin();
     }

     void begin()
     {
	  System.out.println("Enter the string");
	  Scanner sc = new Scanner(System.in);
	  char[] bracs = sc.next().toCharArray();
	  int row = checkIfValid(0,bracs);
	  if(row==-1)
	       System.out.println("wrong");
	  else
	       System.out.println("right");
     }

     int checkIfValid(int i , char[] bracs)
     {
	  for( ;i<bracs.length;i++)
	  {
	       System.out.println("i here "+i);
	       int j;
	       if(bracs[i] == '('||bracs[i]=='{'||bracs[i]=='[')
	       {
		    //System.out.println("ichar here "+bracs[i]);
		    j=checkIfValid(i+1,bracs);
		    if(j==-1)
			 return j;
		    System.out.println("ichar here "+bracs[i]);
		    System.out.println("jchar here "+bracs[j]);
		    switch(bracs[i])
		    {
			 case '(':
			      if(bracs[j]!=')')
			      {
				   return -1;
			      }
			      break;
			 case '[':
			      if(bracs[j]!=']')
			      {
				   return -1;
			      }
			      break;
			 case '{':
			      if(bracs[j]!='}')
			      {
				   return -1;
			      }
			      break;
		    }
		    i=j;
	       }
	       else 
	       {
		    return i;
	       }
	  }
	  return 0;
     }
}
