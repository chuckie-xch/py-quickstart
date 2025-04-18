from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        t = [0.0] * target
        st = []
        for i, v in enumerate(position):
            t[position[i]] = (target - v) / speed[i]

        for i, v in enumerate(t):
            if v != 0.0:
                while st and v >= t[st[len(st) - 1]]:
                    st.pop()
                st.append(i)

        return len(st)
