/*
1. You are given a number n, representing the size of array a.
2. You are given n numbers, representing elements of array a.
3. You are given another number d.
4. You are required find the ceil and floor of d in the array a.

Ceil is defined as value in array which is just greater than d. If an element equal to d exists that will be considered as ceil.
Floor is defined as value in array which is just lesser than d. If an element equal to d exists that will be considered as floor.
Asssumption - Array is sorted.

Input:
10 -> n
1, 5, 10, 15, 22, 33, 40, 42, 55, 66
34 -> d

Output:
40 -> ceil
33 -> floor
*/

import java.io.*;
import java.util.*;

public class Main{

public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    int[] arr = new int[n];
    for(int i = 0; i < n; i++){
       arr[i] = Integer.parseInt(br.readLine());
    }
    int data = Integer.parseInt(br.readLine());

    int left = 0;
    int right = arr.length - 1;
    int ceil = 0;
    int floor =  0;

    // Use Binary search to shrink the low (floor) and high (ceil)
    while(left <= right){
       int mid = (left + right) / 2;
       if(data > arr[mid]){
         left = mid + 1;
         floor = arr[mid];
       } else if(data < arr[mid]){
         right = mid - 1;
         ceil = arr[mid];
       } else  {
         floor = arr[mid];
         ceil = arr[mid];
         break;
       }
    }

    System.out.println(ceil); 
    System.out.println(floor);
 }

}