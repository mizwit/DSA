class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        strs.sort()
        first, last = strs[0], strs[-1]
        if first == last: return first
        res = ""
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]: return res
            res += first[i]
        return res