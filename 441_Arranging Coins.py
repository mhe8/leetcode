"""
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

x
xx
xxx
xxxx

Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
 
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        # binary search problem
        left, right = 1, n
        ans = 0

        # Visit all the values from left to the right
        while left <= right:
            # mid is the layer of the coins 
            mid = (left + right) // 2
            # Calculate the total count of the coins that needed for the cube with mid layers
            total_coin = (mid / 2) * (mid + 1)

            if total_coin > n:
                right  = mid - 1
            else:
                left  = mid + 1
                ans = max(mid, ans)

        return ans
