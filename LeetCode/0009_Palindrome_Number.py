class Solution:
    def isPalindrome(self, x: int) -> bool:
        if 0 <= x < 10: return True
        if x < 0 or x % 10 == 0: return False

        i, res = x, 0
        while i != 0:
            res = (res * 10) + (i % 10)
            i //= 10
        return res == x