class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute force: Have two for loops, and for every index, check if the two indicies add up to target, and make sure they are distinct
        nums_map = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_map:
                return [nums_map[target - nums[i]], i]
            nums_map[nums[i]] = i
        


        