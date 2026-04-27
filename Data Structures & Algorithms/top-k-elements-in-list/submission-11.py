class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = defaultdict()
        for num in nums:
            if num in occ:
                occ[num] += 1
            else:
                occ[num] = 1
        answer = []
        counter = 0
        occ = dict(sorted(occ.items(), key=lambda item: item[1]))
        keys = list(occ.keys())
        keys.reverse()
        while counter < k:
            answer.append(keys[counter])
            counter += 1
        return answer

                
        
        
 
        
      
        

