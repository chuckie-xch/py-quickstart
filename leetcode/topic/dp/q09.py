from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        f = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            j = min(n, questions[i][1] + i + 1)
            f[i] = max(f[i + 1], f[j] + questions[i][0])

        return f[0]
