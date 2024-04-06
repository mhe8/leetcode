"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1)
        if k == len(nums):
            return nums

        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key = count.get)
        # key=count.get: A key function to specify how to extract the comparison key from each element. In this case, it's count.get, which retrieves the value associated with each element in the count dictionary.