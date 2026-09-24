class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, k = 0, 1
        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:
                nums[k] = nums[i + 1]
                k += 1
            i += 1
        return k