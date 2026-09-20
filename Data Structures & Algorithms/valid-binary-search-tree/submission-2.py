# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
              
        valMin = -1000000000 
        valMax = 1000000000
        def checkValid(root, valMin, valMax):
            if not root:
                return True
            if root.val <= valMin or root.val >= valMax:
                return False
            return checkValid(root.left, valMin, root.val) and checkValid(root.right, root.val, valMax)        

        return checkValid(root.left, valMin, root.val) and checkValid(root.right, root.val, valMax)
        



        