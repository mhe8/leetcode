"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

Two pointers, left increase and loop has right pointer to be moved to left
"""

left = 0

for right in range(len(nums)):
    if nums[right] != 0:
        nums[right], nums[left] = nums[left], nums[right]
        left += 1

return nums
