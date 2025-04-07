from typing import List


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def f(d: int) -> int:
            cnt, pre = 1, price[0]
            for p in price:
                if p >= pre + d:
                    cnt += 1
                    pre = p
            return cnt

        price.sort()

        left, right = 0, price[0] + (price[-1] - price[0]) // (k - 1)
        while left <= right:
            mid = left + (right - left) // 2
            if f(mid) >= k:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1
