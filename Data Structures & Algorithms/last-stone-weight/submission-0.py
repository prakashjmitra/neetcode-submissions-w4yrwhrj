class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = stones
        heapq.heapify_max(maxHeap)
        while len(maxHeap) >= 2:
            if len(maxHeap) == 2:
                if maxHeap[0] == maxHeap[1]:
                    return 0
                return abs(maxHeap[0] - maxHeap[1])
            else:
                if maxHeap[1] > maxHeap[2]:
                    second_max = maxHeap[1]
                else:
                    second_max = maxHeap[2]
                if maxHeap[0] == second_max:
                    heapq.heappop_max(maxHeap)
                    heapq.heappop_max(maxHeap)
                else:
                    thing_1 = heapq.heappop_max(maxHeap)
                    thing_2 = heapq.heappop_max(maxHeap)
                    heapq.heappush_max(maxHeap,abs(thing_1 - thing_2))
        return maxHeap[0]



        