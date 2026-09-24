class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        output = []
        for i in range(numRows):
            output.append(self.build_from_row(s, numRows, i))
        return "".join(output)
    
    def build_from_row(self, s: str, t: int, n: int) -> str:
        out = []
        cur = n
        if n == 0 or n == t - 1:
            while cur < len(s):
                out.append(s[cur])
                cur += 2 * (t - 1)
        else:
            isEven = True
            while cur < len(s):
                out.append(s[cur])
                if isEven:
                    cur += 2 * (t - n - 1)
                    isEven = False
                else:
                    cur += 2 * n
                    isEven = True
        return "".join(out)