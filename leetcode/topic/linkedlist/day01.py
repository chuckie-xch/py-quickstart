from typing import Optional

from leetcode.datastruct.list_node import ListNode


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        head = self.reverse(head)
        bit, ans = 0, 0
        while head is not None:
            ans += pow(2, bit) * head.val
            bit += 1
            head = head.next
        return ans

    def reverse(self, head: Optional[ListNode]) -> ListNode:
        pre, next = None, None
        while head is not None:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre
