/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package atice;

/**
 *
 * @author simpli
 */
public class Stack_Array {
    
    int top = -1;
    public static void main(String[] args)
    {
        Stack_Array sa = new Stack_Array();
        sa.begin();
    }
    void begin()
    {
        int A[] = new int[10];
        System.out.println("pushing");
        for (int i = 0; i < 12; i++) {
            push(A, i);
        }
        System.out.println("popping");
        for (int i = 0; i < 12; i++) {
            pop(A);
        }
    }
    
    void push(int A[],int key)
    {
        if(top >= A.length-1){
            System.out.println("over flow");
        }
        else{
            top++;
            A[top] = key;
        }
    }
    void pop(int A[])
    {
        if(top==-1){
            System.out.println("underflow");
        }
        else{
            System.out.println("top element is "+A[top]);
            top--;
        }
    }
}
