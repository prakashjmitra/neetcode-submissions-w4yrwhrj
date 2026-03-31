class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size = len(nums1) + len(nums2)
        half = size//2
        if len(nums2) < len(nums1):
            nums1,nums2 = nums2,nums1
        l = 0
        r = len(nums1) - 1
        while True:
            i = (l+r)//2
            j = half - i - 2

            first_left = nums1[i] if i >=0 else float("-infinity")
            first_right = nums1[i+1] if (i+1) < len(nums1) else float("infinity")
            second_left = nums2[j] if j>=0 else float("-infinity")
            second_right = nums2[j+1] if (j+1) < len(nums2) else float("infinity")
            if first_left <= second_right and second_left <= first_right:
                if size%2:
                    return min(first_right,second_right)
                return (max(first_left,second_left) + min(first_right,second_right)) /2
            elif first_left>second_right:
                r = i - 1
            else:
                l = i + 1


