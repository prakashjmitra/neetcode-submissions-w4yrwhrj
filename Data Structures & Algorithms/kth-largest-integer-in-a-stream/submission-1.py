class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.array = []
        self.integer = k
        for i in range(len(nums)):
            self.array.append(nums[i])


    def add(self, val: int) -> int:
        self.array.append(val)
        self.array = sorted(self.array, reverse = True)
        for i in range(len(self.array)):
            print(self.array[i])
        print("done")
        answer = self.array[self.integer -1]
        return answer


        
