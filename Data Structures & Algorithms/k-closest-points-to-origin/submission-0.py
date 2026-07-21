class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        pts = []
        for i in range(len(points)):
            print(points[i][0])
            print(points[i][1])
            dist = math.sqrt(((points[i][0])**2 + (points[i][1])**2))
            distances.append([dist,points[i]])
            print([dist, points[i]])
        new_distances = sorted(distances,key = lambda x:x[0])
        print("###")
        for z in range(len(new_distances)):
            print(new_distances[z])
        answer = []
        counter = 0
        while counter < k:
            answer.append(new_distances[counter][1])
            counter += 1
        return answer


        

        