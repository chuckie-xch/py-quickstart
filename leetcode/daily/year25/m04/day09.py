from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        mn = min(nums)
        if mn < k:
            return -1
        return len(set(nums)) - (k == mn)

    def minOperations2(self, nums: List[int], k: int) -> int:
        st = set()
        for x in nums:
            if x < k:
                return -1
            if x > k:
                st.add(x)
        return len(st)
