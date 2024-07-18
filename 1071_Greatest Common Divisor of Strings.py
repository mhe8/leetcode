"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""

def gcd(s1, s2):

    # cal the remainder
    remainder = len(s1)%len(s2)

    # if condition of remainder.
    if remainder == 0:
        return s2
    else:
        return gcd(s2, s1[-remainder:])
    
class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        # Edge check
        if str1 + str2 != str2 + str1:
            return ""
        if str1 == "" or str2 == "":
            return ""
        else:
            if len(str1) >= len(str2):
                return gcd(str1, str2)
            else:
                return gcd(str2, str1)