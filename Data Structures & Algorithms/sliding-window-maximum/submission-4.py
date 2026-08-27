class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        first_pointer = 0
        second_pointer = k - 1
        new_list = []
        for i in range(len(nums)):
            new_list.append([nums[i] * - 1, i])
        answer = []
        heapq.heapify(new_list)
        while second_pointer <= len(nums) -1:
            heapq.heappush(new_list, [nums[second_pointer] * -1, second_pointer])
            while new_list[0][1] > second_pointer or new_list[0][1] < first_pointer:
                element = heapq.heappop(new_list)
            answer.append(new_list[0][0] * -1)
            second_pointer += 1
            first_pointer += 1
        return answer
        