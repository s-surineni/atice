class GreedyActivSelec
{
     int[] s = {0,1,3,0,5,3,5,6,8,8,2,12};
     int[] f = {0,4,5,6,7,9,9,10,11,12,14,16};
     int[] a = new int[s.length];

     public static void main(String[] args)
     {
	  GreedyActivSelec gas = new GreedyActivSelec();
	  gas.begin();
     }
     void begin()
     {
	  recurrActSel(0);
	  JavaL jl = new JavaL();
	  jl.display(a);
     }

     void recurrActSel(int curr)
     {
	  int nex = curr + 1;
	  while(nex < s.length)
	  {
	      if(s[nex] >= f[curr])
	      {
		    a[nex] = 1;
		    recurrActSel(nex);
		    return;

	       }
	       nex++;
	  }
     }

}
