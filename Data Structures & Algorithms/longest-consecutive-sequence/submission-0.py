class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = set(nums)
        longest = 0

        for k in answer:
            counter = 0
            if k-1 not in answer:
                length = 0
                while (k + length in answer):
                    length = length + 1
                longest = max(length, longest)
                
        return longest


        