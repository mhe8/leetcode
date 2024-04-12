"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

TC: O(N) SC: O(1)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ans = {}

        if len(s) != len(t):
            return False

        # create the counter for characters
        for i in s: 
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1

        # Match the counts from s to t
        for i in t:
            if i not in ans or ans[i] == 0:
                return False
            ans[i] -= 1

        # if nothing return, False doesn't return, then it must be True
        return True