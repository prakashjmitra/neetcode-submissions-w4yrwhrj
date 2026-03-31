class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = -1
        answer = [0] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            answer[i] = maximum
            maximum = max(maximum, arr[i])

        return answer

