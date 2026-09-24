class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                for j in range(len(needle)):
                    if i + j >= len(haystack) or needle[j] != haystack[i + j]: break
                else: return i
        return -1
    
        # return haystack.find(needle)