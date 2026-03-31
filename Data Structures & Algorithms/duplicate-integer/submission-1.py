class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occ = {}
        for i in range(0, len(nums),1):
            if(nums[i] not in occ):
                occ[nums[i]] = 1
            else:
                return True
        return False

