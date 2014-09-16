import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
 class TestClass14 {
      public static void main(String[] args) {
	  BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	  try {
	      Integer testCase = Integer.parseInt(br.readLine());
	      while(testCase--!=0){
		    String input=br.readLine();
     		  Long a=Long.parseLong(input.split(" ")[0]);
     		  Long b=Long.parseLong(input.split(" ")[1]);
	         Long m=Long.parseLong(input.split(" ")[2]);
	   a=a+m-(a%m);
         if(b%m!=0)
     b=b-(b%m);
  Long ans=1+((b-a)/m);
  System.out.println(ans);
  }
 } catch (NumberFormatException e) {
     e.printStackTrace();
     } catch (IOException e) {
      // TODO Auto-generated catch block
  e.printStackTrace();
}
      }
 }


