/*
1. You've to check whether a given number is prime or not.
2. Take a number "t" as input representing count of input numbers to be tested.
3. Take a number "n" as input "t" number of times.
4. For each input value of n, print "prime" if the number is prime and "not prime" otherwise.
*/

import java.util.*;
  
  public class Main{
  
  public static void main(String[] args) {
      Scanner scn = new Scanner(System.in);
      int t = scn.nextInt();
      
      // Loop to take 't' inputs
      for(int i = 0; i < t; i++){
          int n = scn.nextInt();
          
          // Start checking for factors from 2
          int div = 2;
          /* All factors of a number n repeat after root n
          Eg. 24 --> 1*24, 2*12, 3*8,  4*6 (repeat factors after root of 24 = 4.~)
                     6*4,  8*3,  12*2, 24*1 
          */
          while(div * div <= n){
              // If you find a divisor before root n, then break since not prime
              if(n % div == 0){
                  break;
              }
              div++;
          }
          
          if(div * div > n){
              System.out.println("prime");
          } else {
              System.out.println("not prime");
          }
      }
  
   }
  }


                        