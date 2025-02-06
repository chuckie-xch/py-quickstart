from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        path = [0] * n
        on_path = [False] * n

        def dfs(i: int) -> None:
            if i == n:
                ans.append(path.copy())
                return
            for j, on in enumerate(on_path):
                if on or (j > 0 and nums[j] == nums[j - 1] and not on_path[j - 1]):
                    continue
                path[i] = nums[j]
                on_path[j] = True
                dfs(i + 1)
                on_path[j] = False

        dfs(0)
        return ans
