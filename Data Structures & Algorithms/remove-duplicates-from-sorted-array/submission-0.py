class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap = {}
        counter = 0
        left = 0
        while left <= len(nums) - 1:
            if nums[left] != None:
                if nums[left] in hashmap:
                    print(nums[left], "reached")
                    print(left, len(nums))
                    nums.pop(left)
                    left = left - 1
                else:
                    hashmap[nums[left]] = 1
            left = left + 1
        
                

        return len(nums)
        