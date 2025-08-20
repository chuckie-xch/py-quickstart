from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pre_max, pre_min, ans = nums[0], nums[0], nums[0]
        for x in nums[1:]:
            cur_max = max(x, x * pre_max, x * pre_min)
            cur_min = min(x, x * pre_max, x * pre_min)
            ans = max(ans, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return ans
