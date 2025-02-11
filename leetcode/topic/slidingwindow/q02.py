from math import inf
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = -inf
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if i + 1 < k:
                continue
            maxSum = max(maxSum, sum)
            sum -= nums[i - k + 1]

        return maxSum / k
