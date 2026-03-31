class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = collections.defaultdict(int)
        for n in nums:
            numbers[n] = numbers[n] + 1
            if numbers[n] > 1:
                return True
            
        for k in numbers:
            print(k, numbers[k])
        return False
