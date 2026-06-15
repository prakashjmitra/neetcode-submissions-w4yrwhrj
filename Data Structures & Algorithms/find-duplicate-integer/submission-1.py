class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        maps = {}
        for num in nums:
            if num in maps:
                return num
            else:
                maps[num] = 1
        
            