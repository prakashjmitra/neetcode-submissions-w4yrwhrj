class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occ = {}
        for i in range(0, len(nums),1):
            if(nums[i] not in occ):
                occ[nums[i]] = 1
            else:
                occ[nums[i]] +=1


        for key in occ:
            if occ[key] > 1:
                return True
        return False