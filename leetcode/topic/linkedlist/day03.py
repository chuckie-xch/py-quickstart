from typing import Optional

from leetcode.datastruct.list_node import ListNode


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        p0 = dummy
        for _ in range(left - 1):
            p0 = p0.next

        pre = None
        cur = p0.next
        for _ in range(right - left + 1):
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        p0.next.next = cur
        p0.next = pre

        return dummy.next
