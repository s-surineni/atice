package atice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class LongestCommomSubsequence {
	
	char[] S1Array;
	char[] S2Array;
	public static void main(String[] args) 
	{
		LongestCommomSubsequence lcs = new LongestCommomSubsequence();
		lcs.begin();
	}
	
	void begin()
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter first string");
		try {
			String s1 = br.readLine();		
			S1Array = s1.toCharArray();
			System.out.println("Enter second string");
			String s2 = br.readLine();
			S2Array = s2.toCharArray();
			int c[][] = new int[s1.length()+1][s2.length()+1];
			char[][] lcs = new char[s1.length()][s2.length()];
			for(int i = 0;i< s1.length();i++)
			{
				for(int j = 0; j< s2.length();j++)
				{
					if(S1Array[i] == S2Array[j])
					{
						c[i+1][j+1] = c[i][j]+1;
						lcs[i][j] = 'c';
					}
					else if(c[i][j+1]>c[i+1][j])
					{
						c[i+1][j+1] = c[i][j+1];
						lcs[i][j] = 'u';
						
					}
					else
					{
						c[i+1][j+1] = c[i+1][j];
						lcs[i][j] = 'l';
					}
				}
			}
			System.out.println(c[c.length-1][c[0].length-1]);
			printLCS(lcs, s1.length()-1, s2.length()-1);
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	void printLCS(char[][] LCS,int r,int c)
	{
		
		if(r<0 || c<0)
		{
			return;
		}
		System.out.println(LCS[r][c]);
		if(LCS[r][c]=='c')
		{
			
			printLCS(LCS, r-1, c-1);
			System.out.print(S1Array[r]);
			
		}
		else if(LCS[r][c]=='l')
		{
			printLCS(LCS, r, c-1);
		}
		else
		{
			printLCS(LCS, r-1, c);
		}
	}
}
