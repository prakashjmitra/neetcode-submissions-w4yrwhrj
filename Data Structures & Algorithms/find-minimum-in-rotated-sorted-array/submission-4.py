class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums)-1
        l = 0
        minimum = nums[len(nums)-1]
        while l<=r:
            mid = (l+r)//2
            if nums[mid] < minimum: 
                minimum = nums[mid]
                r = mid -1
            elif nums[mid] > minimum:
                l = mid + 1
            else:
                return minimum
        return minimum
            
            