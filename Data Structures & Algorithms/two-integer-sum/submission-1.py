class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        left = 0
        right = 1
        while left <= len(nums) - 1:
            if right == len(nums) -1:
                right = 0
                left = left + 1 
                continue
            if left != right:
                if (nums[left] + nums[right] == target):
                    first = min(left,right)
                    if right == first:
                        second = left
                    else:
                        second = right
                    output.append(first)
                    output.append(second)
                    break
            right = right + 1
        return output

  

        