class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        for value in nums:
            if value not in occ:
                occ[value] = 1
            else:
                occ[value] += 1
        new_occ = dict(sorted(occ.items(), key = lambda item: item[1], reverse = True))
        answers = []
        for key in new_occ:
            if k > 0:
                answers.append(key)
                k = k - 1
        
                
        return answers

                
        
        
 
        
      
        

