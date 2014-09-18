package atice;

import java.util.Scanner;
class LongIncSubSeq
{
     public static void main(String[] args)
     {
          LongIncSubSeq lis = new LongIncSubSeq();
          lis.begin();
     }     

     void begin()
     {
          JavaL jl = new JavaL();
          Scanner sc = new Scanner(System.in);
          System.out.println("Enter no of ele in seq");
          int seqlen=sc.nextInt();
          System.out.println("Please enter the sequence seperated by spaces");
          int seq[] = new int[seqlen];
          for(int i = 0;i<seqlen;i++)
          {
               seq[i]=sc.nextInt();
          }
          int len[]=new int[seqlen];
          int prev[]=new int[seqlen];

          int maxestInd = 0;
          for(int i = 0;i<seqlen;i++)
          {
               prev[i]= -1;
               int max = 0;
               for(int j = 0;j<i;j++)
               {
                    if(seq[i]>seq[j])
                    {
                         if(max<len[j])
                         {
                              max=len[j];
                              prev[i]=j;
                         }
                         
                    }
               }
               len[i]=++max;
               if(len[maxestInd]<len[i])
                    maxestInd = i;
          }
          jl.display(prev);
          System.out.println("maxest "+maxestInd);
          System.out.println("len is " + len[maxestInd]);
          System.out.println("sequence");
          int lent = len[maxestInd];
          for(int i = 0;i<lent;i++)
          {
               
               System.out.print(seq[maxestInd]);
               maxestInd = prev[maxestInd];
          }
          
     }
}
