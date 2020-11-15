/*
1. You are given n number of bulbs. They are all switched off. A weird fluctuation in voltage hits 
   the circuit n times. In the 1st fluctuation all bulbs are toggled, in the 2nd fluctuation every 2nd bulb is toggled, in the 3rd fluctuation every 3rd bulb is toggled and so on. You've to find which bulbs will be switched on after n fluctuations.
2. Take as input a number n, representing the number of bulbs.
3. Print all the bulbs that will be on after the nth fluctuation in voltage.
*/

import java.util.*;
  
  public class Main {
  
  	  public static void main(String[] args) {
  	  	  Scanner scn = new Scanner(System.in);
          int n = scn.nextInt();
          
          /* 
          Key is that only perfect squares will stay ON. Why?
          Since only the numbers which are perfect squares have Odd number (2n + 1 factors)
          of factors, the rest of the numbers have Even number of factors (2n factors)

          */
          for(int i = 1; i * i <= n; i++){
              System.out.println(i * i);
          }
  	  }
  }