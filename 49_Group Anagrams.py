"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    ans_dict = defaultdict(list)

    for str in strs:
        sorted_str = ''.join(sorted(str))
        ans_dict[sorted_str].append(str)

    return list(ans_dict.values())