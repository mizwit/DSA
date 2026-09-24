class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        end = []
        for i in range(k):
            end.append(nums[len(nums) - k + i])
        for i in range(len(nums) - k - 1, -1, -1):
            nums[i + k] = nums[i]
        j = 0
        for i in range(k):
            nums[i] = end[j]
            j += 1
        return