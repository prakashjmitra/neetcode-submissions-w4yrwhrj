class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify_max(minHeap)
        for i in range(len(points)):
            squared = (points[i][0] ** 2) + (points[i][1] ** 2)
            heapq.heappush_max(minHeap, [squared, points[i]])
            if len(minHeap) > k:
                heapq.heappop_max(minHeap)
        answer = []
        for j in minHeap:
            print(j, j[0])

        for row in minHeap:
            answer.append(row[1])
        return answer


        

        