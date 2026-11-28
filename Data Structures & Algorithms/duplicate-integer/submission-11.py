class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Brute force solution: Would require O(n^2) as there would be a need for a nested for loop, bottleneck is when arrays become large, hashmap alleviates this
        nums_seen = set()
        for num in nums:
            if num in nums_seen:
                return True
            nums_seen.add(num)
        return False
        
        
