"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
"""

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        # define two intial numbers
        min = float('inf')
        sec_min = float('inf')

        # extreme case
        if len(nums)<3:
            return False
        
        # traverse
        for num in nums:
            if num < min:
                min = num
            elif num < sec_min and num > min:
                sec_min = num
            else:
                return True
            
        return False