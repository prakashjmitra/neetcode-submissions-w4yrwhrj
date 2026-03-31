class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        count_dict = defaultdict(int)
        for i in range(len(nums)):
            if target - nums[i] in count_dict:
                print("Reached",i)
                output.append(count_dict[target-nums[i]])
                output.append(i)
                return output
            count_dict[nums[i]] = i
        