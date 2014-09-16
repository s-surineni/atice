import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

class GenFile
{
     public static void main(String[] args)
     {
	  String input = System.getProperty("user.dir")+"/input.txt";
	  File inFil = new File(input);
	  try
	  {
	       inFil.createNewFile();
	       FileWriter fw = new FileWriter(inFil);
	       fw.write("150"+'\n');
		  for(int i = 1;i<=5;i++)
		  {
		       for(int j =1;j<=50;j++)
		       {
			    fw.write(1+" "+j+" "+i+'\n');
		       }
		  }
	       fw.close();
	  }
	  catch(IOException e)
	  {
	       System.out.println("Cannot create file");
	  }
     }
}
