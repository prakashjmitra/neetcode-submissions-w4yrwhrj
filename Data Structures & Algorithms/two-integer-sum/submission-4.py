class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap.values():
                for key in hashmap:
                    if hashmap[key] == target - nums[i]:
                        if key > i:
                            return [i, key]
                        else:
                            return [key, i]
            else:
                hashmap[i] = nums[i]
        