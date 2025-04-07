from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        ans = 0
        nums.sort()

        for i in range(n - 1, 1, -1):
            k = nums[i]
            l, r = 0, i - 1
            while l < r:
                s = nums[l] + nums[r]
                if s <= k:
                    l += 1
                else:
                    ans += r - l
                    r -= 1

        return ans
