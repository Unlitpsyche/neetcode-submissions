class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = "".join(ch for ch in s if ch.isalnum()).lower()
        b = a[::-1]
        if a == b:
            return True
        return False