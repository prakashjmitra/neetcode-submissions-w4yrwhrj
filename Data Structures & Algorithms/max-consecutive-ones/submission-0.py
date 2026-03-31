class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        check = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            else:
                check = max(check, counter)
                counter = 0
        check = max(check, counter)
        return check

        