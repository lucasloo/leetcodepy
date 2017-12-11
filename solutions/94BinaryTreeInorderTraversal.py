# Given a binary tree, return the inorder traversal of its nodes' values.

# For example:
# Given binary tree [1,null,2,3],

#    1
#     \
#      2
#     /
#    3

# return [1,3,2].

# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Recursive
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(node):
            if node == None:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        res = []
        inorder(root)
        return res
    
    # iteratively
    def inorderTraversal(self, root):
        stack = []
        res = []
        current = root
        while current or len(stack) > 0:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            res.append(current.val)
            current = current.right
        return res
                
