"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
 
"""

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        idx, n = 0, len(arr)

        # if len < 3 then it will be invalid
        if n < 3:
            return False
        
        # Go up and check the up trend
        while idx + 1 < n and arr[idx] < arr[idx + 1]:
            idx += 1

        # check if this peak position is in the head or the tail of the list
        if idx == 0 or idx == n - 1:
            return False
        
        # Continue to check the go down trend
        while idx + 1 < n and arr[idx] > arr[idx + 1]:
            idx += 1

        return idx == n - 1 # check if the final index equal the entire array's length