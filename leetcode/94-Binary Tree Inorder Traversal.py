"""
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
 
Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        def traversal(node):
            if not node:
                return
            if node.left: traversal(node.left)
            output.append(node.val)
            if node.right: traversal(node.right)

        output = []
        traversal(root)
        return output




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    Solution 1
    preorder traversal, inorder traversal, postorder traversal
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        ans = []
        def recur(node):
            # If root is None, return None
            if not root:
                return
            if node.left: recur(node.left)
            ans.append(node.val)
            if node.right: recur(node.right)
        recur(root)
        return ans
