from typing import List

from leetcode.datastruct.tree_node import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root: Optional[TreeNode]):
            if root:
                dfs(root.left)
                res.append(root.val)
                dfs(root.right)

        dfs(root)
        return res
