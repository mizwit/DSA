class Solution:
    def rotateArray(self, nums, k: int) -> None:
        k = k % len(nums)
        end = []
        for i in range(k):
            end.append(nums[i])
        for i in range(len(nums) - k):
            nums[i] = nums[i + k]
        j = 0
        for i in range(len(nums) - k, len(nums)):
            nums[i] = end[j]
            j += 1
        return