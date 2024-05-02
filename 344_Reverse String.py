"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

two pointers: same arrya, two pointers, two directions when meet...

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:

        # two pointers
        left, right = 0, len(s) - 1

        # extreme cases
        if len(s) == 0:
            return []
        elif len(s) == 1:
            return s
        
        # iteration
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s