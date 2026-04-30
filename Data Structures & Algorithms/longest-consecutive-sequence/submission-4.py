class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = []
        nums.sort()
        if len(nums) == 0:
            return 0
        for j in range(len(nums)):
            longest = 1
            mini = nums[j]
            for i in range(len(nums)):
                if nums[i] == (mini + 1):
                    longest += 1
                    mini = nums[i]
            answer.append(longest)


                
        return max(answer)


        