class Solution:
    def secondLargestElement(self, nums):
        l = nums[0]
        sl = -10001

        for n in nums:
            if n > l:
                sl = l
                l = n
            if n < l and n > sl:
                sl = n

        if l == sl or sl == -10001:
            return -1
        return sl