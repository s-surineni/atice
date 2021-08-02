import java.io.*;

class Solution {
  public static void main(String[] args) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int itr = Integer.parseInt(br.readLine());
    for (int i = 0; i < itr; i++) {
      String[] s = br.readLine().split(" ");
      long D = Long.parseLong(s[0]);
      long d = Long.parseLong(s[1]);
      long P = Long.parseLong(s[2]);
      long Q = Long.parseLong(s[3]);
      long newN = D / d;
      long remDays = D % d;
      long newRate = newN * Q;

      long ans = (remDays * newRate) + ((P * D) + (((newN * ((newN - 1) * Q)) / 2) * d));
      System.out.println(ans);
    }
  }
}