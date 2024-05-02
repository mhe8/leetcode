"""
Given two integer arrays nums1 and nums2, return an array of their 
intersection
. Each element in the result must be unique and you may return the result in any order.

# Two pointers in two seperate arrays but they will have same directions of moving.

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # sort the arrays for better performance
        nums1.sort()
        nums2.sort()

        # two pointers
        left1, left2 = 0, 0
        ans = 0

        while left1 < len(nums1) and left2 < len(nums2):
            if nums1[left1] == nums2[left2]:
                # confirm if dup
                if nums1[left1] not in ans:
                    ans.append(nums1[left1])
                
                left1 += 1
                left2 += 1

            elif nums1[left1] < nums2[left2]:
                left1 += 1
            else:
                left2 += 1

        return ans