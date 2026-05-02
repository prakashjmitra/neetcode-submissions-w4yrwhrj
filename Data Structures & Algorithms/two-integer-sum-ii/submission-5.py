class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        while left <= len(numbers) -1:
            right = len(numbers) -1
            while right > left:
                if numbers[left] + numbers[right] == target:
                    return [left + 1, right + 1]
                right = right - 1
            left = left + 1
            
        
