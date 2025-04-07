from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        left, right, ans, totalA, totalB = 0, len(plants) - 1, 0, capacityA, capacityB
        while left < right:
            if totalA < plants[left]:
                ans += 1
                totalA = capacityA
            if totalB < plants[right]:
                ans += 1
                totalB = capacityB
            totalA -= plants[left]
            totalB -= plants[right]
            left += 1
            right -= 1

        if left == right and max(totalB, totalA) < plants[left]:
            ans += 1

        return ans
