from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        start, end = -1, len(s)
        map = defaultdict(int)

        for c in t:
            map[c] += 1

        l, need = 0, len(t)
        for r, x in enumerate(s):
            map[x] -= 1
            if map[x] >= 0:
                need -= 1

            if need == 0:
                while map[s[l]] < 0:
                    map[s[l]] += 1
                    l += 1
                if end - start > r - l:
                    start = l
                    end = r
                map[s[l]] += 1
                need += 1
                l += 1
        return "" if start < 0 else s[start: end + 1]
