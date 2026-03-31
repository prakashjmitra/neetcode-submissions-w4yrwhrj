class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        num_zeroes = 0
        product = 1
        for n in nums:
            if n == 0:
                num_zeroes += 1
            else:
                product *= n
        if num_zeroes >= 2:
            return [0] * len(nums)
        elif num_zeroes == 1:
            for n in nums:
                if n == 0:
                    answer.append(int(product))
                else:
                    answer.append(0)
        else:
            for n in nums:
                answer.append(int(product/n))
        return answer


