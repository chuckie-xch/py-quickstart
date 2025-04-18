from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        st = []
        for i in range(2 * n):
            index = i % n
            x = nums[index]
            while st and x > nums[st[len(st) - 1]]:
                j = st.pop()
                ans[j] = x
            if i < n:
                st.append(i)

        return ans
