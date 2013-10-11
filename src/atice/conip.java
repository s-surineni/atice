/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package atice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 *
 * @author vinnu
 */
public class conip {
    public static void main(String args[])
throws IOException
{
char c;
BufferedReader br = new
BufferedReader(new InputStreamReader(System.in));
System.out.println("Enter characters, 'q' to quit.");
int count=0;
do {
c = (char) br.read();
count++;
System.out.println("see " + count);
//System.out.println(c);
} while(c != 'q');
System.out.println(c);

}
}
