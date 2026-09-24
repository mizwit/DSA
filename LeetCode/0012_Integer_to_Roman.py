class Solution:
    def intToRoman(self, num: int) -> str:
        x, res = 1, []

        while True:
            val = ((num % (x * 10)) - (num % x)) // x
            if x > num and val == 0: break
            x *= 10
            if val == 0: continue

            match x:
                case 10:
                    res.append(self.roman_for_digit(val, 'I', 'V', 'X'))
                case 100:
                    res.append(self.roman_for_digit(val, 'X', 'L', 'C'))
                case 1000:
                    res.append(self.roman_for_digit(val, 'C', 'D', 'M'))
                case _:
                    res.append("M" * val)

        res.reverse()
        return "".join(res)
    
    def roman_for_digit(self, digit, first, middle, last):
        if digit < 4: return first * digit
        if digit == 4: return first + middle
        if digit == 5: return middle
        if digit < 9: return middle + (first * (digit - 5))
        if digit == 9: return first + last