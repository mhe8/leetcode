""""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

""""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

# ================SOLUTION 1 ===================
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # Define a list
        ans = []

        # Define a root
        if root is None:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
# ================SOLUTION 2 ===================
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Traverse inorder : Root -> left -> right
        def inorder_helper(node):
            if node:
                # Traverse left subtree
                inorder_helper(node.left)

                # Root
                ans.append(node.val)

                # Traverse right subtree
                inorder_helper(node.right)

        # Use helper to traverse
        inorder_helper(root)

        return ans