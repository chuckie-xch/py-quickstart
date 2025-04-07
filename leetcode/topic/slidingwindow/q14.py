from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        lMax, rMax, l, r = height[0], height[n - 1], 0, n - 1
        ans = 0
        while l <= r:
            if lMax < rMax:
                ans += max(0, lMax - height[l])
                lMax = max(lMax, height[l])
                l += 1
            else:
                ans += max(0, rMax - height[r])
                rMax = max(rMax, height[r])
                r -= 1
        return ans
