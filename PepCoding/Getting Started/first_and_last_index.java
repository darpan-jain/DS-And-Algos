/*
1. You are given a number n, representing the size of array a.
2. You are given n numbers, representing elements of array a.
3. You are given a number d, representing the search element.
4. You have to output the first and last index of that element in the array.

Asssumption - Array is sorted. Array may have duplicate values.

Input:
15 -> n 
1, 5, 10, 15, 22, 33, 33, 33, 33, 33, 40, 42, 55, 66, 77
33 -> d

Output:
5 -> first
9 -> last
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

    int left = 0; // low
    int right = arr.length - 1; // high
    int fi = -1;

    // Begin searching using binary search

    // Finding last index
    while(left <= right){
       int mid = (left + right) / 2;
       if(data > arr[mid]){
            left = mid + 1;
       } else if(data < arr[mid]){
            right = mid - 1;
       } else  {
        /*
        Here, the data = mid. Normal binary search would stop at this condition.
        For our solution, we keep moving the high (right) to the left in search of
        a better last index for our data
        */
            fi = mid;
            right = mid - 1;
       }
    }

    // Finding first index
    left = 0;
    right = arr.length - 1;
    int li = -1;
    while(left <= right){
       int mid = (left + right) / 2;
       if(data > arr[mid]){
         left = mid + 1;
       } else if(data < arr[mid]){
         right = mid - 1;
       } else  {
        /*
        Same condition as before. But here we move low (left) to the right,
        to search for a better first index of data (search element)
        */
          li = mid;
          left = mid + 1;
       }
    }

    System.out.println(fi); 
    System.out.println(li);
 }