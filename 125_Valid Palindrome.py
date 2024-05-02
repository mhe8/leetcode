"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Use two pointers
"""

class Solution:
    """
    Scan the valid numbers/characters first if not return False - > create a helper function
    Then scan the palindrome
    """

    def helper(self, letter):
        return (
            (ord('A') <= ord(letter) <= ord('Z')) or
            (ord('a') <= ord(letter) <= ord('z')) or
            (ord('0') <= ord(letter) <= ord('9'))
        )
    
    def isPalindrome(self, s: str) -> bool:

        left, right = 0,len(s) - 1

        while left < right :

            while left < right and not self.helper(s[left]):
                left += 1
            while left < right and not self.helper(s[right]):
                right -= 1

            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
            
        return True