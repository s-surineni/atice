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
          System.out.println("after input");
          jl.display(seq);
          int len[]=new int[seqlen];
          for(int i = 0;i<seqlen;i++)
          {
               int max = 0;
               for(int j = i-1;j>=0;j--)
               {
                    if(seq[i]>seq[j])
                    {
                         max =len[j];
                         break; 
                    }
               }
               len[i]=++max;
               System.out.println("each it "+len[i]);


          }
          System.out.println("len is " + len[seqlen-1]);
     }
}
