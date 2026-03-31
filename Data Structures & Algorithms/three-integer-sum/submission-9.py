class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == None:
            return []
        nums.sort()
        answers = []
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums)- 1
            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                if summ < 0:
                    left = left + 1
                elif summ > 0:
                    right = right - 1
                else:
                    if i != left and left != right and i != right and [nums[i], nums[left], nums[right]] not in answers:
                        answers.append([nums[i], nums[left], nums[right]])
                    left = left + 1
                    right = right - 1

        return answers
                

                
   
        