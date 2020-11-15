/*
    1. You are required to display the prime factorization of a number.
    2. Take as input a number n.
    3. Print all its prime factors from smallest to largest.
*/

import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        
        /* Factors repeat after root of number i.e. i*i
           Theorem: If p*q = n
           Then p > root n and q > root n is NOT possible
        */
        for(int i = 2; i * i <= n; i++){
            while(n % i == 0){
                System.out.print(i + " ");
                n = n / i;
            }
        }
        
        // Since it's a prime number, it broke the loop early
        // Print the number as its prime factor
        if(n != 1)
            System.out.print(n);
	}
}