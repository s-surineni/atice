package atice;

import java.util.Scanner;
import java.util.regex.Pattern;

public class QuickSort
{
     public static void main(String[] a)
     {
	  QuickSort qs = new QuickSort();
	  qs.begin();
     }

     void begin()
     {
	  System.out.println("Enter the numbers you want to sort seperated"
	       +" by ','");
	  Scanner sc = new Scanner(System.in);
	  String iLine = sc.nextLine();
	  sc = new Scanner(iLine);
	  //sc.useDelimiter("\\s*,*\\s");
	  sc.useDelimiter(Pattern.compile("\\s*,\\s*"));
	  int noOfEle=0;
	  for( ;sc.hasNextInt();noOfEle++)
	  {
	       sc.nextInt();
	  }
	  int nos[] =new int[noOfEle];
	  sc = new Scanner(iLine);
	  //sc.useDelimiter("\\s*,*\\s");
	  sc.useDelimiter(Pattern.compile("\\s*,\\s*"));
	  for(int i=0 ;sc.hasNextInt();i++)
	  {
	       nos[i]=sc.nextInt();
	  }
	  display(nos);
	  quickSort(nos,0,nos.length-1);
	  display(nos);
     }

     int[] quickSort(int[] nos,int st,int end)
     {
         if(st<end)
	  {
	       int indOfP = partition(nos,st,end);
	       quickSort(nos,st,indOfP-1);
	       quickSort(nos,indOfP+1,end);
	  }
	  return nos;
     }

     public char[] quickSort(char[] nos,int st,int end)
     {
         if(st<end)
	  {
	       int indOfP = partition(nos,st,end);
	       quickSort(nos,st,indOfP-1);
	       quickSort(nos,indOfP+1,end);
	  }
	  return nos;
     }

     int partition(int[] nos,int st,int end)
     {
	  int pivInd = st-1;
	  for(int i = st;i<= end;i++)
	  {
	       if(nos[i]<=nos[end])
	       {
		    pivInd++;
		    int tmp = nos[pivInd];
		    nos[pivInd] = nos[i];
		    nos[i]=tmp;
	       }
	  }
	  return pivInd;
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
     void display(int[] Arr) {
	  System.out.println("Start of Display");
	  for (int trk = 0; trk < Arr.length; trk++) {

	       System.out.println(Arr[trk] + " ");
	  }
	  System.out.println("End of Display");
     }
}
