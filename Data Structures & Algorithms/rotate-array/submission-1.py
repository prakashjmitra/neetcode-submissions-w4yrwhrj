class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_list = []
        for i in range(len(nums)):
            new_list.append(nums[((len(nums) - k)+i) % len(nums)])
        for y in range(len(new_list)):
            nums[y] = new_list[y]

        