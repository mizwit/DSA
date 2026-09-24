class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end, max = 0, 0, 0
        c_map = {}
        while end < len(s):
            if start <= c_map.get(s[end], -1) <= end:
                start = c_map[s[end]] + 1
            c_map[s[end]] = end
            end += 1
            max = end - start if (end - start) > max else max
        return max