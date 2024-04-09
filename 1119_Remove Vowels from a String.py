"""
Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

 

Example 1:

Input: s = "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: s = "aeiou"
Output: ""

"""

class Solution:
    def removeVowels(self, s: str) -> str:

        if len(s) == 0 :
            return []
        
        ans = []

        for n in s:
            if n not in "aeiou": 
                ans.append(n)

        return ''.join(ans) # made mistake here