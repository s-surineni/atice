/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package atice;

/**
 *
 * @author vinnu
 */
public class QueArr {
    
    int head,tail;
    
    public static void main(String[] args){
        QueArr qr = new QueArr();
        qr.begin();
    }
    
    void begin()
    {
        int A[] = new int[10];
        for (int i = 0; i < 12; i++) {
            enQue(A, i);
        }
        
        for (int i = 0; i < 12; i++) {
            deQue(A);
        }
    }

    public QueArr() {
        head = tail = 0;
    }
    
    void enQue(int A[],int ele)
    {
        if((tail+1)%A.length == head)
        {
            System.out.println("overflow");
        }
        else
        {
            A[tail] = ele;
            tail++;
        }
        
    }
    
    void deQue(int A[])
    {
        if(head == tail)
        {
            System.out.println("underflow");
        }
        else{
            System.out.println(A[head]);
            head++;
            
        }
        
    }
}
