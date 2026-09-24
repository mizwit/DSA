class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        closest = len(nums) - 1
        if target < nums[0]: return 0
        if target > nums[closest]: return len(nums)
        
        left, right = 0, len(nums) - 1
        while left <= right:
            half = (right + left) // 2
            if nums[half] == target: return half
            elif nums[half] < target: left = half + 1
            else:
                right = half - 1
                if nums[half] <= nums[closest]: closest = half
        return closest
    
    # Simpler solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     left, right = 0, len(nums) - 1
    #     while left <= right:
    #         half = (right + left) // 2
    #         if nums[half] == target: return half
    #         elif nums[half] < target: left = half + 1
    #         else: right = half - 1
    #     return left