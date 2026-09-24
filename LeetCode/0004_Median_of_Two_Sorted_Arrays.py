class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        first, second = 0, 0
        merged = [] 
        while (first < len(nums1)) and (second < len(nums2)):
            if nums1[first] < nums2[second]:
                merged.append(nums1[first])
                first += 1
            else:
                merged.append(nums2[second])
                second += 1
        merged = merged + nums1[first:]
        merged = merged + nums2[second:]

        median = merged[len(merged)//2] if len(merged) % 2 != 0 else (merged[len(merged)//2] + merged[(len(merged)//2) - 1]) / 2
        return float(median)