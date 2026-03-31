class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        nums.sort()
        for i in range(0, len(nums),1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while l < r:
                if nums[l] + nums[r] + nums[i] > 0:
                    r = r -1
                elif nums[l] + nums[r] + nums[i] < 0:
                    l = l + 1
                else:
                    solutions.append([nums[i], nums[l],nums[r]])
                    l = l + 1
                    while nums[l] == nums[l-1] and l < r:
                        l = l + 1
        return solutions

                
   
        