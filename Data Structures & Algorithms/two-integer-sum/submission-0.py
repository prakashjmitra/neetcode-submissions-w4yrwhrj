class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = 0
        answer = []
        while counter < len(nums) -1:
            first = nums[counter]    
            for i in range(counter, len(nums),1):
                if (first + nums[i] == target and i != counter):
                    answer.append(counter)
                    answer.append(i)
            counter = counter + 1
        return answer



        