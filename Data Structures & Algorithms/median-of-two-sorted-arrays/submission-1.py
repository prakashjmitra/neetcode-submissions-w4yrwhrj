class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for element in nums2:
            nums1.append(element)
        nums1.sort()
        if len(nums1) %2 == 1:
            mid = (0 + len(nums1)-1)//2
            return float(nums1[mid])
        else:
            mid = (0 + len(nums1)-1)//2
            mid2 = mid + 1
            average = (nums1[mid] + nums1[mid2])/2
            return average
