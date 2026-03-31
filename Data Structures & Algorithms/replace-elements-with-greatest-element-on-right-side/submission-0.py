class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) -1):
            right = arr[i+1:]
            arr[i] = max(right)
        arr[len(arr)-1] = -1
        return arr