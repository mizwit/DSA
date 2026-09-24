class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1 # left and right pointers
        max = 0

        while r > l:
            right, left = height[r], height[l]
            if right > left:
                cur = left * (r - l)
                l += 1
            else:
                cur = right * (r - l)
                r -= 1
            max = cur if cur > max else max

        return max  