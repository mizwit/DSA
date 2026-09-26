class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        sum = 0
        for n in nums:
            sum += n
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        return expected_sum - sum