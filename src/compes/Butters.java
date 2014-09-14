package compes;

//http://www.hackerearth.com/problem/algorithm/criminals-little-deepu-and-little-kuldeep-1/

import java.util.Scanner;
import atice.JavaL;


public class Butters {
    Scanner sc ;
    JavaL jl = new JavaL();
    
    public static void main(String[] a)
    {
        Butters b = new Butters();
        b.begin();
    }
    
    void begin()
    {
        sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int i = 0; i < tc; i++) 
        {
            int boxes = sc.nextInt();
            int[] high = new int[boxes];
            for (int j = 0; j < boxes; j++) 
            {
                high[j] = sc.nextInt();
            }
            quickSort(high, 0, boxes-1);
            //System.out.println("after quick");
            //jl.display(high);
            boxes = condense(high,boxes);
            System.out.println(boxes);
        }
    }
    
    int condense(int[] high,int boxes)
    {
        boolean change = false;
        for (int i = 0; i < high.length-1; i++) 
        {
            
            if(high[i]<high[i+1])
            {
                change = true;
                high[i]=-1;
                boxes--;
            }
        }
                
        if(change && boxes!= (high.length+1))
        {
            high[high.length-1]=-1;
            //System.out.println("after condense");
            //jl.display(high);
            //System.out.println("boxes "+boxes);
            boxes = newHigh(high,boxes-1);   
            return boxes;
            
        }
        return boxes;
    }
    
    int newHigh(int[] high,int siz)
    {
        if(siz==0)
            return siz+1;
        int[] nH = new int[siz];
        for (int i = 0,j=0; i < high.length-1; i++) {
            if(high[i]!=-1)
            {
                nH[j]=high[i];
                j++;
            }
        }
        //System.out.println("after nh");
        //jl.display(nH);
        //System.out.println("boxes "+siz);
        siz = condense(nH, siz+1);
        return siz;
    }
    void quickSort(int[] nos,int st,int end)
     {
         if(st<end)
	  {
	       int indOfP = partition(nos,st,end);
	       quickSort(nos,st,indOfP-1);
	       quickSort(nos,indOfP+1,end);
	  }
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
}
