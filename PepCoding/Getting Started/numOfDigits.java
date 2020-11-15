/*
1. You've to count the number of digits in a number.
2. Take as input "n", the number for which the digits has to be counted.
3. Print the digits in that number.
*/

import java.util.*;
  
  public class Main{
  
  public static void main(String[] args) {
  
  Scanner scn = new Scanner(System.in);
  int n = scn.nextInt();
  
  // Digit keeps a count of how many times a number can be 
  // divided by 10 before being reduced to a value of 0
  int digit = 0;
  while(n!=0){
      n = n/10;
      digit++;
  }
  
  // That value is the number fo digits in a number
  System.out.println(digit);
  
   }
  }


                        