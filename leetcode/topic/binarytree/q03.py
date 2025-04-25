from typing import List, Optional

from leetcode.datastruct.tree_node import TreeNode


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root: Optional[TreeNode]):
            if root:
                dfs(root.left)
                dfs(root.right)
                res.append(root.val)

        dfs(root)
        return res
