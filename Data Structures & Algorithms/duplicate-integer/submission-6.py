class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occ = {}
        for n in nums:
            if n in occ:
                return True
            else:
                occ[n] = 1
        return False
        
        
