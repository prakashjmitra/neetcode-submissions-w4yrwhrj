class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = []
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if (nums[left] + nums[right] + nums[i] == 0):
                    answers.append([nums[i], nums[left],nums[right]])
                    left = left + 1
                    right = right - 1
                    while left < len(nums) -1  and nums[left - 1] == nums[left]:
                        left = left + 1
                    while right > i and nums[right + 1] == nums[right]:
                        right = right - 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right = right - 1
                else:
                    left = left + 1
        return answers

