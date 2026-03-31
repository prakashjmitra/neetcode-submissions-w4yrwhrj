class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        second = len(numbers) - 1
        while first < len(numbers):
            print(numbers[first],numbers[second])
            if numbers[first] + numbers[second] == target:
                return [first+1,second+1]
            if second <= first:
                first = first + 1
                second = len(numbers) - 1
                continue
            second = second - 1
        
