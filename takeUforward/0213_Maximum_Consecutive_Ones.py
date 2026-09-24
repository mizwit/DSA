class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max = 0
        counter = 0
        for n in nums:
            if n == 1:
                counter += 1
            if n == 0:
                counter = 0
            if counter > max:
                max = counter
        return max