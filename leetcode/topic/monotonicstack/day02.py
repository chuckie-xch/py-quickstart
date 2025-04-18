from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0] * n
        st = []
        for i, x in enumerate(prices):
            while st and x <= prices[st[-1]]:
                j = st.pop()
                ans[j] = prices[j] - x
            st.append(i)

        while st:
            j = st.pop()
            ans[j] = prices[j]

        return ans

    def finalPrices2(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0] * n
        st = []
        for i in range(n - 1, -1, -1):
            x = prices[i]
            while st and x < prices[st[-1]]:
                st.pop()
            if st:
                ans[i] = x - prices[st[-1]]
            else:
                ans[i] = prices[i]
            st.append(i)
        return ans
