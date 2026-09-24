class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            # base case: not found
            if left >= len(nums) or right < 0: return -1

            half = (right - left) // 2
            start, middle, end = nums[left], nums[half], nums[right]

            # base cases: found
            if target == start: return left
            if target == middle: return half
            if target == end: return right

            # recursive case: 1
            if target > middle:
                if target > start or target < end: return binary_search(half + 1, right - 1)
                else: return binary_search(left + 1, half - 1)

            # recursive case: 2
            if target < middle:
                if target > end: return binary_search(left + 1, half - 1)
                else: return binary_search(half + 1, right - 1)
                
        return binary_search(0, len(nums) - 1)