import string


class Solution:
    def lengthOfLongestSubstring(self, s: string) -> int:
        n = len(s)
        if n < 2:
            return n

        ans, l, r = 0, 0, 1
        cnt = [0] * 128
        cnt[ord(s[l])] += 1

        while r < n:
            cur = s[r]
            cnt[ord(cur)] += 1
            while cnt[ord(cur)] > 1:
                cnt[ord(s[l])] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1

        return ans
