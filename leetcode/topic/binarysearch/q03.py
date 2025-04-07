from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        def lowerIndex() -> int:
            l, r = 0, n - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] <= 0:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        def higherIndex() -> int:
            l, r = 0, n - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] >= 0:
                    r = mid - 1
                else:
                    l = mid + 1
            return r

        lower = lowerIndex()
        higher = higherIndex()
        return max(n - lower, higher + 1)
