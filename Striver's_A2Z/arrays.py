# https://takeuforward.org/practice/dsa/linear-search
class Solution:
    def linearSearch(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


# https://takeuforward.org/practice/dsa/largest-element
class Solution:
    def largestElement(self, nums):
        l = nums[0]
        for n in nums:
            if n > l:
                l = n
        return l


# https://takeuforward.org/practice/dsa/second-largest-element
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


# https://takeuforward.org/practice/dsa/maximum-consecutive-ones
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


# https://takeuforward.org/practice/dsa/left-rotate-array-by-one
class Solution:
    def rotateArrayByOne(self, nums):
        first = nums[0]
        for i in range(len(nums) - 1):
            nums[i] = nums[i + 1]
        nums[len(nums) - 1] = first
        return



# https://takeuforward.org/practice/dsa/left-rotate-array
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


# https://takeuforward.org/practice/dsa/move-zeros-to-end
class Solution:
    def moveZeroes(self, nums):
        i = 0
        for n in nums:
            if n != 0:
                nums[i] = n
                i += 1
        for x in range(i, len(nums)):
            nums[x] = 0
        return


# https://takeuforward.org/practice/dsa/remove-duplicates-from-sorted-array
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        for n in nums:
            if n > nums[i]:
                i += 1
                nums[i] = n
        return i + 1


# https://takeuforward.org/practice/dsa/find-missing-number
class Solution:
    def missingNumber(self, nums):
        sum = 0
        for n in nums:
            sum += n
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        return expected_sum - sum

# https://takeuforward.org/practice/dsa/union-of-two-sorted-arrays
class Solution:
    def unionArray(self, nums1, nums2):
        union = []
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                cur = nums1[i]
                i += 1 
            elif nums1[i] > nums2[j]:
                cur = nums2[j]
                j += 1
            else:
                cur = nums1[i]
                i += 1
                j += 1
            if (not union or cur != union[-1]):
                union.append(cur)
        while i < n1:
            cur = nums1[i]
            if not union or cur != union[-1]:
                union.append(cur)
            i += 1
        while j < n2:
            cur = nums2[j]
            if not union or cur != union[-1]:
                union.append(cur)
            j += 1
        return union


# https://takeuforward.org/practice/dsa/intersection-of-two-sorted-arrays
class Solution:
    def intersectionArray(self, nums1, nums2):
        inter = []
        i, j = 0, 0
        n, m = len(nums1), len(nums2)
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
            else:
                inter.append(nums1[i])
                i += 1
                j += 1
        return inter

