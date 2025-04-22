from typing import Optional

from leetcode.datastruct.list_node import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.findMid(head)
        head2 = self.reverseList(mid)
        while head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True

    def findMid(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head):
        pre = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre
