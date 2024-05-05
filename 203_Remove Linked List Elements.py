"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

linked list
create a dummy node prior to the head

remove a node in the linked list:
curr.next = curr.next.next
Move to the next node
curr = curr.next
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # create a dummy node
        dummy = ListNode(-1)
        dummy.next = head

        # set the dummy node as the starting point
        curr = dummy

        # traversal
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next # remove the created dummy node from the result