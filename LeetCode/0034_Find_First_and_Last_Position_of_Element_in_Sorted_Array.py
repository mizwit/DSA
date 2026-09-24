class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        l, r = 0, len(nums) - 1
        while l <= r:
            half = r - l // 2
            if nums[half] < target:
                l = half + 1
            elif nums[half] > target:
                r = half - 1
            else:
                for lh in range(half, -1, -1):
                    if nums[lh] != target: break
                    res[0] = lh
                for rh in range(half, len(nums)):
                    if nums[rh] != target: break
                    res[1] = rh
                break
        return res
    
    # Using binary search after finding target
    
    # def searchRange(self, nums: list[int], target: int) -> list[int]:
    #     lh, rh = -1, -1
    #     l, r = 0, len(nums) - 1

    #     while l <= r:
    #         half = r - l // 2
    #         if nums[half] < target:
    #             l = half + 1
    #         elif nums[half] > target:
    #             r = half - 1
    #         else:
    #             lh, rh, = half, half
    #             nl, nr = half + 1, half - 1

    #             while l <= nr:
    #                 nh = nr - l // 2
    #                 if nums[nh] < target:
    #                     l = nh + 1
    #                     continue
    #                 if nums[nh] == target:
    #                     lh = nh
    #                 nr = nh - 1
              
    #             while nl <= r:
    #                 nh = r - nl // 2
    #                 if nums[nh] < target:
    #                     nl = nh + 1
    #                     continue
    #                 if nums[nh] == target:
    #                     rh = nh
    #                 r = nh - 1
    #             break
            
    #     return [lh, rh]