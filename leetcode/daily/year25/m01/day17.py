from cmath import inf
from typing import List


class Solution:
    def mininumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = inf
        bit = [0] * 32

        def check():
            for i in range(30, -1, -1):
                if bit[i] > 0 and (((k >> i) & 1) == 0):
                    return True
                if bit[i] == 0 and (((k >> i) & 1) == 1):
                    return False
            return True

        l, r = 0, -1
        while r < n:
            while check() and l <= r:
                ans = min(ans, r - l + 1)
                for i in range(30):
                    bit[i] -= ((nums[l] >> i) & 1)
                l += 1

            r += 1
            if r == n:
                break

            for i in range(30):
                bit[i] += ((nums[r] >> i) & 1)

        return ans if ans != inf else -1
