class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        count = [0] * 26
        maxFreq = 0

        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            count[idx] += 1
            maxFreq = max(maxFreq, count[idx])

            while (right - left + 1) - maxFreq > k:
                idx = ord(s[left]) - ord('A')
                count[idx] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans

