class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal = s[:1]
        for i in range(len(s)):
            loop_times = 1
            if i < len(s) - 1 and s[i] == s[i + 1]:
                loop_times += 1
            
            for j in range(loop_times):
                if j == 0:
                    left, right = i - 1, i + 1
                    cur = s[i:right]
                else:
                    left, right = i - 1, i + 2
                    cur = s[i:right]

                # check if there is a palindrome in current substring
                while True:
                    if left < 0 or right >= len(s):
                        break
                    if s[left] == s[right]:
                        cur = s[left:right + 1]
                        left -= 1
                        right += 1
                    else:
                        break

                pal = cur if len(cur) > len(pal) else pal
        return pal