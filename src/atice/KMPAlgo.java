package atice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class KMPAlgo {
	JavaL jl;
	public static void main(String[] a)
	{
		KMPAlgo ka = new KMPAlgo();
		ka.begin();
	}
	
	void begin()
	{
		jl = new JavaL();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int txtLen ;
		int wrdLen ;
		System.out.println("Please enter text to look in ");
		
		try {
			String txt = br.readLine();
			char[] txtArr = txt.toCharArray();
			txtLen = txtArr.length;
			System.out.println("Enter the word to look for");
			String wrd = br.readLine();
			char[] wrdArr = wrd.toCharArray();
			wrdLen = wrdArr.length;	
			int[] lsp = new int[wrdLen+1];
			fillLSP(lsp,wrdLen,wrdArr);
			printIndexes(txtArr,txtLen,wrdArr,wrdLen,lsp);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
	
	void printIndexes(char[] txt,int tlen,char[] wrd,int wlen,int[] lsp)
	{
		wlen--;
		for(int i=0,j=0;i<tlen;i++)
		{
//			System.out.print(txt[i]);
//			System.out.println(wrd[j]);
			if(txt[i]==wrd[j])
			{
				if(j ==wlen)
				{
					
					System.out.println(i-j);
					j = 0;
				}
				j++;
			}
			else if(j==0)
			{
				
			}
			else
			{
				i--;
				j = lsp[j];
			}
		}
	}
	
	void fillLSP(int[] lsp,int len,char[] wrd)
	{
		for(int i = 1;i<len;i++)
		{
			int j = 0;
			if(wrd[i] == wrd[j])
			{
				lsp[i+1]=1;
			}
			if(lsp[i]!=0)
			{
				j=j+lsp[i];
				if(wrd[i] == wrd[j])
				{
					lsp[i+1]= lsp[i]+1;
				}
			}
		}
		//jl.display(lsp);
	}
}
