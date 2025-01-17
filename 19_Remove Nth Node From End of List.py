"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Delete the node from the right to the left, the nth position

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

    dummy = ListNode(0, head)
    left = dummy
    right  = head

    while n > 0 and right:
      right = right.next
      n -= 1

    while right:
      left = left.next
      right = right.next

    # delete the node
    left.next = left.next.next

    return dummy.next