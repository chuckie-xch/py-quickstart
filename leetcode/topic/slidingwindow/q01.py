class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        ans = vowel = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(n):
            if s[i] in vowels:
                vowel += 1
            if i + 1 < k:
                continue

            ans = max(ans, vowel)

            out = s[i - k + 1]
            if out in vowels:
                vowel -= 1

        return ans
