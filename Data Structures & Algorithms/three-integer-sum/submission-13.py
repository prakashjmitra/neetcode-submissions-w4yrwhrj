class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = []
        for i in range(len(nums) - 1):
            first = i + 1
            last = len(nums) -1
            while first < last:
                if nums[i] + nums[first] + nums[last] == 0:
                    if [nums[i], nums[first], nums[last]] not in answers:
                        answers.append([nums[i], nums[first], nums[last]])
                    first = first + 1
                    last = last - 1
                elif nums[i] + nums[first] + nums[last] > 0:
                    last = last - 1
                else:
                    first = first + 1
        return answers


                

                
   
        