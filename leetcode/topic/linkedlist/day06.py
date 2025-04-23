from leetcode.datastruct.list_node import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, dummy
        while n > 0:
            right = right.next
            n -= 1
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
