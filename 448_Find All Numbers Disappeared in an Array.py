"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]

"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        hash_table = {}
        ans = []

        # put the data into hash
        for num in nums:
            hash_table[num] = 1

        for num in range(1, len(nums) + 1):
            if num not in hash_table:
                ans.apend(num)

        return ans