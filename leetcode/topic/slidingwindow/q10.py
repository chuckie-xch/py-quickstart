from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = -x
        for num in nums:
            target += num

        if target < 0:
            return -1

        left, s, ans = 0, 0, -1
        for r, cur in enumerate(nums):
            s += cur
            while s > target:
                s -= nums[left]
                left += 1
            if s == target:
                ans = max(ans, r - left + 1)

        return -1 if ans == -1 else len(nums) - ans
