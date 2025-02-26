class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans, left = 0, 0
        cnt = [0] * 128
        for r, cur in enumerate(s):
            cnt[ord(cur)] += 1
            while cnt[ord(cur)] > 2:
                cnt[ord(s[left])] -= 1
                left += 1
            ans = max(ans, r - left + 1)
        return ans
