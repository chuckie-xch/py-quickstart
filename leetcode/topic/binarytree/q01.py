from typing import List, Optional

from leetcode.datastruct.tree_node import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []

        def dfs(root: Optional[TreeNode]):
            if root is None:
                return
            arr.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return arr
