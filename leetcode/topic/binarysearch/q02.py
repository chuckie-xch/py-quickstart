from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l, r = 0, n - 1
        while l <= r and r - l + 1 > k:
            if abs(arr[l] - x) <= abs(arr[r] - x):
                r -= 1
            else:
                l += 1
        return arr[l:r + 1]
