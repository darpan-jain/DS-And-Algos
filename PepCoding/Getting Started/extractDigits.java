/*
1. You've to display the digits of a number.
2. Take as input "n", the number for which digits have to be displayed.
3. Print the digits of the number line-wise.
*/

import java.util.*;
    
    public class Main {
    
        public static void main(String[] args) {
            Scanner scn = new Scanner(System.in);
            int n = scn.nextInt();
            

            // First we calculate the number of digits in a number
            // The power = (10 ^ number of digits) is the value used to extract the quotient of the number
            // which will be extracted digits at each point
            int power = 1;
            int temp = n;
            while (temp >= 10) {
                temp /= 10;
                power *= 10;
            }

            /* 
            We stop when the power becomes zero, NOT when the number becomes zero
            Why?
            For numbers like 7600, 820 etc. if we stop when number becomes zero, we will miss the last digits which are zero.
            Instead, when we check for power being zero, the value of power is as shown below:
            Eg. n = 7600, power = 1000 (10^3)
            Power      Number    Remainder     Digit/Quotient
            1000        7600        600             7
            100          600         00             6
            10            00          0             0
            1              0          0             0
            0 --> Loop stops
            */   

            temp = n;
            while(power != 0) {
                int digit = temp / power;
                System.out.println(digit);
    
                temp = temp % power; 
                power = power / 10;
            }
        }
    }