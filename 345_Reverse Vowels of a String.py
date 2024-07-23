"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
"""

class solution:
    def reverseVowels(self , s : str) -> str:
        ans = list(s)
        vowels_list = set('AEIOUaeiou') # unordered unique element sets, with faster time complexity than list

        left, right  = 0, len(ans) - 1

        while left < right:
            while left < right and ans[left] not in vowels_list:
                left += 1
            while left < right and ans[right] not in vowels_list:
                right -= 1
            ans[left], ans[right] = ans[right], ans[left]
            left += 1
            right -= 1

        return ''.join(ans)