import java.util.*;
    
    public class Main {
    
        public static void main(String[] args) {
            Scanner scn = new Scanner(System.in);
            int num1 = scn.nextInt();
            int num2 = scn.nextInt();
            
            // Save original numbers for calculating LCM
            int tnum1 = num1;
            int tnum2 = num2;
            
            // Divide n1 by n2, use rem as next n2 (dividend)
            while(tnum1 % tnum2 != 0){               
                int rem = tnum1 % tnum2;
                tnum1 = tnum2;
                tnum2 = rem;
            }
            
            // Last number remaining is GCD
            int gcd = tnum2;
            // Use formula GCD * LCM = n1 * n2 
            int lcm = (num1 * num2)/gcd;
    
            System.out.println(gcd);
            System.out.println(lcm);
    	    }
    }