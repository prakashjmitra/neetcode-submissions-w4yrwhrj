class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap.values():
                return True
            hashmap[i] = nums[i]
        return False
            
        
        
