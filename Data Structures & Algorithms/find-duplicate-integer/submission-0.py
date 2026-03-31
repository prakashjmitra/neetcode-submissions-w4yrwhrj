class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        thing = {}
        for num in nums:
            if num not in thing:
                thing[num] = 1
            else:
                return num
        