class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            product = 1
            number = nums[i]
            for j in range(len(nums)):
                if nums[j] == 0 and i == j:
                    pass
                else:
                    product *= nums[j]
            if number == 0:
                pass
            else:
                product /= number
            answer.append(int(product))
        return answer


