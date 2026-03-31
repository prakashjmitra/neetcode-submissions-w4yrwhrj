class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        products = []
        product = 1
        for i in range(0,len(nums),1):
            product = product * nums[i]
            prefix.append(product)
        product2 = 1
        for w in range(len(nums)):
            postfix.append(1)
        for j in range(len(nums)-1,-1,-1):
            product2 = product2 * nums[j]
            postfix[j] = product2
       
        for k in range(0,len(nums),1):
            if k-1 < 0:
                products.append(postfix[k+1])
            elif k + 1 == len(nums):
                products.append(prefix[k-1])
                break
            else:
                products.append(prefix[k-1] * postfix[k+1])
        return products
