from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        return self.dfs(head, root) | self.isSubPath(head, root.left) | self.isSubPath(head, root.right)

    def dfs(self, head, root):
        if head is None:
            return True
        if root is None:
            return False
        if root.val == head.val:
            return self.dfs(head.next, root.left) | self.dfs(head.next, root.right)
        return False
