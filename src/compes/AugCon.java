/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package atice;

import java.util.Scanner;

/**
 *
 * @author vinnu
 */
public class AugCon {
    public static void main(String[] args)
    {
        AugCon ac = new AugCon();
        ac.begin();
    }
    
    void begin()
    {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for(int i =0;i<tc;i++)
        {
            int ind = sc.nextInt();
            int swaps = sc.nextInt();
            int[][] swpCount = new int[3][swaps];
            countSwaps(ind,swaps,swpCount);
            
            
        }
    }
    
    void countSwaps(int indx,int swp,int[][] spCnt)
    {
        if(swp == 0)
        {
            spCnt[indx][spCnt[indx].length]=spCnt[indx][swp];
        }
        else
        {
            spCnt[indx][spCnt[indx].length]=spCnt[indx][swp];
        }
    }
}
