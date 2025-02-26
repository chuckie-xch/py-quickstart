from typing import List


class Solution:
    def numOfSubArrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans, sum = 0, 0
        threshold = threshold * k
        for i in range(len(arr)):
            sum += arr[i]
            if i + 1 < k:
                continue

            ans += 1 if sum >= threshold else 0
            sum -= arr[i - k + 1]

        return ans
