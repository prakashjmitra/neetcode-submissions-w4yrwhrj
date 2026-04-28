class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = 1
        second_answer = 1
        output = []
        z = 0
        for num in nums:
            answer *= num
            if num == 0:
                z += 1
        if answer == 0:
            if z > 1:
                for i in range(len(nums)):
                    output.append(0)
            else:
                for j in range(len(nums)):
                    if nums[j] == 0:
                        continue
                    second_answer *= nums[j]
                for k in range(len(nums)):
                    if nums[k] == 0:
                        output.append(second_answer)
                    else:
                        output.append(0)
        else:
            for x in range(len(nums)):
                output.append(int(answer/nums[x]))


        
        return output
        
        
                

        


