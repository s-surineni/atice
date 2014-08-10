/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
//package atice;

/**
 *
 * @author umaram
 */
import java.io.IOException;

public class test {
    
    final static String ESC = "\033[";
public static void main(String[] args){
    int i = 1;
    i = i<<31;
    //System.out.print(ESC + "2J");
    //System.out.pril String ANSI_CLS = "\u001b[2J";
final String ANSI_CLS = "\u001b[2J";
final String ANSI_HOME = "\u001b[H";
	            System.out.print(ANSI_CLS + ANSI_HOME);
		            System.out.flush();//ntln(i);
    try
    {
    Runtime.getRuntime().exec("pwd");
    }
    catch(IOException e)
    {
	 System.out.println("ecep");
    }
}
    
}
