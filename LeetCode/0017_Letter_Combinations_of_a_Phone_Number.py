class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_map = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], 
                   '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        if len(digits) == 0: return []
        return self.get_combinations(digits, num_map, 0)
    
    def get_combinations(self, digits, map, index):
        # base case
        if index == len(digits) - 1: return map[digits[index]]

        # recursion
        old_res = self.get_combinations(digits, map, index + 1)
        res = []
        for c1 in map[digits[index]]:
            for c2 in old_res:
                res.append(c1 + c2)
        return res