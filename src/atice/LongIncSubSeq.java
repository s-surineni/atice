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
          Scanner sc = new Scanner(System.in);
          System.out.println("Enter no of ele in seq");
          System.out.println("Please enter the sequence seperated by spaces");
          int seqlen=sc.nextInt();
          int seq[] = new int[seqlen];
          for(int i = 0;i<seqlen;i++)
          {
               seq[i]=sc.nextInt();
          }
          for(int i = 0;i<seqlen;i++)
          {
               int max = 0;
               for(int j = i;j<i;j++)
               {
                    if(seq[i]>seq[j])
                    {

                    }
               }
          }
     }
}
