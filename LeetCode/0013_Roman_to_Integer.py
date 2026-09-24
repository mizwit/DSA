class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 
                   'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 
                   'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        res = 0
        for sym in symbols:
            while s.startswith(sym):
                res += symbols[sym]
                if len(sym) == 1: s = s[1:]
                else: s = s[2:]
        return res