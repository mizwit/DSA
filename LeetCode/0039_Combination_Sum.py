class Solution:
    def combinationSum(self, candidates: list[int], target: int, output) -> list[list[int]]:
        # debugging
        print(f"For: {candidates} Target = {target}")
        print("Exp:", output)

        # solution
        res = []
        def backtrack(index, ls):
            n = ls[index]

            # Base case 1
            if len(ls) == 1:
                if target % n == 0:
                    res.append([n for _ in range(target // n)])
                return
            
            # Base case 2
            if n == ls[-1]:
                backtrack(ls[1], ls[1:])

                ... 

        for i in range(candidates):
            backtrack(i, candidates[i:])
        return res

        # res = []
        # for i, n in enumerate(candidates):
        #     if n == target: res.append([n])
        #     for j in range(target // n, 1, -1):
        #         for m in candidates:
        #             if (n * j) + m == target: res.append([n for _ in range(j)] + [m])
        #     for m in candidates[i:]:
        #         if m + n == target: res.append([n, m])
        # return res


if __name__ == "__main__":
    s = Solution()
    print("Res:", s.combinationSum(candidates = [2,3,6,7], target = 7, output = [[2,2,3],[7]]), end=f"\n{'-'*30}\n")
    print("Res:", s.combinationSum(candidates = [2,3,5], target = 8, output = [[2,2,2,2],[2,3,3],[3,5]]), end=f"\n{'-'*30}\n")
    print("Res:", s.combinationSum(candidates = [2], target = 1, output = []), end=f"\n{'-'*30}\n")
    print("Res:", s.combinationSum(candidates = [8,7,4,3], target = 11, output = [[8,3],[7,4],[4,4,3]]), end=f"\n{'-'*30}\n")
    print("Res:", s.combinationSum(candidates = [7,3,2], target = 18, output = [[7,7,2,2],[7,3,3,3,2],[7,3,2,2,2,2],[3,3,3,3,3,3],[3,3,3,3,2,2,2],[3,3,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2]]), end=f"\n{'-'*30}\n")