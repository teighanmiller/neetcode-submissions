class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = s.lower()
        r = len(s) - 1
        l = 0

        while l <= r:
            while r > l and not s[r].isalnum():
                r -= 1

            while l < r and not s[l].isalnum():
                l += 1

            if not s[r] == s[l]:
                return False
            l += 1
            r -= 1

        return True 