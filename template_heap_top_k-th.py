"""
Approach 1: If largest k-th, create max_heap, traverse and delete the top element, swap the top if not clear min_heap, repeat until find the top k, then the deleted are the answer
            If smallest k-th, create the min_heap, same approach.
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        return nums[k-1]
    
"""
Approach 2: If largest k-th, create min_heap. traverse. Push the elements into heap, compare the heap size when add the elemtn, if exceed, pop the element of heap.
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
    


    