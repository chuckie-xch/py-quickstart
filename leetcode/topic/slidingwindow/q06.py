from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s, n = 0, len(cardPoints)
        for i in range(k):
            s += cardPoints[i]

        ans = s
        for i in range(1, k + 1):
            s += cardPoints[n - i] - cardPoints[k - i]
            ans = max(ans, s)

        return ans
