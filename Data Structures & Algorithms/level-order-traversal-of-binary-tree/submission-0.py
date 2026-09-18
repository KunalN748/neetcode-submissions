# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.arr = []
        def levelArr(root, level):
            if not root:
                return
            if len(self.arr) < level:
                self.arr.append([])
            self.arr[level-1].append(root.val)
            return levelArr(root.left, level+1) or levelArr(root.right, level+1)
        level = 1
        levelArr(root, level)
        return self.arr


