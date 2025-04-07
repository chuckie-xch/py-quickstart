from typing import List


def lower_bound(nums: List[int], target: int) -> int:
    n = len(nums)
    l, r = 0, n - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = lower_bound(nums, target)
        return i if i < len(nums) and nums[i] == target else -1
