"""
Approach: get the max val in each row by saving the level and its corresponding nodeVals in a hashmap. Or directly
saved into a res array which always saves the maxVal in each index. Straighforward DFS with level as an arg.
t.c. => O(n)
s.c. => O(h) where h is the height of the tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root, level):
            if not root:
                return 
            
            if len(res) == level:
                res.append(root.val)
            else:
                res[level] = max(res[level], root.val)
            
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        dfs(root, 0)
        return res