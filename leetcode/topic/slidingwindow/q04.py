from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        n = len(nums)
        ans = [-1] * n
        s = 0
        for i in range(n):
            s += nums[i]
            if i < 2 * k:
                continue
            ans[i - k] = s // (2 * k + 1)
            s -= nums[i - 2 * k]

        return ans
