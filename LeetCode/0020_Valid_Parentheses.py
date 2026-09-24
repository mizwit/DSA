class Solution:
    def isValid(self, s: str) -> bool:
        open = ['(', '{', '[']
        closed = [')', '}', ']']
        stack = []
        for bracket in s:
            if bracket in open: stack.append(bracket)
            if bracket in closed:
                if len(stack) == 0 or closed.index(bracket) != open.index(stack.pop()): return False
        if len(stack) != 0: return False
        return True