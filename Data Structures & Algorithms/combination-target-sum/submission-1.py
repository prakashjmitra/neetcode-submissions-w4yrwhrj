class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(path, summ, index):
            if summ == target:
                results.append(path[:])
                return
            if index >= len(nums) or summ > target:
                return 
            #Decision 1
            path.append(nums[index])
            backtrack(path, nums[index] + summ, index)
            path.pop()

            #Decision 2
            backtrack(path, summ, index+1)
            
        backtrack([], 0, 0)
        return results
