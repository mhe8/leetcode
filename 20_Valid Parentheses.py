"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
  def isValid(self, s: str) -> bool:

    # better to use hash map than hash set
    stack = []

    # map
    dict_map = {
      "(" : ")",
      "[" : "]",
      "{" : "}"
    }

    for char in s:
        if char in dict_map.keys():
            if not stack or stack.pop != dict_map[char]:
               return False
        elif char in dict_map.values():
            stack.append(char)
        else:
           return False
    return True
           