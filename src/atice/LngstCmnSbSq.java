import java.util.Scanner;
class LngstCmnSbsq
{
     public static void main(String[] args)
     {
	  LngstCmnSbsq lcs = new LngstCmnSbsq();
	  lcs.begin();
     }

     void begin()
     {
	  Scanner sc = new Scanner(System.in);
	  String s1;
	  String s2;
	  System.out.println("Enter the first string");
	  s1 = sc.next();
	  System.out.println("Enter the second string");
	  s2 = sc.next();
	  int s1_len = s1.length();
	  int s2_len = s2.length();
	  char[] s1Arr = s1.toCharArray();
	  char[] s2Arr = s2.toCharArray();
	  int[][] subSeqLen = new int[s1_len+1][s2_len+1];
	  int[][] subSeq = new int [s1_len][s2_len];
     }
}
