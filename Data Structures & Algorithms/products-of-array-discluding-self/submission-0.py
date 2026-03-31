class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        counter = 0
        for j in range(len(nums)):     
            product = 1 
            for i in range(0, len(nums),1):
                if counter != i:
                    product = product * nums[i]
            products.append(product)
            counter += 1
        return products
        