class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values = {}
        test = [[] for i in range(len(nums) + 1)]
        answers = []
        
        for num in nums:
            values[num] = 1 + values.get(num,0)
        for num, count in values.items():
            test[count].append(num)

        for b in range(len(test) - 1, 0, -1):
            for n in test[b]:
                answers.append(n)
                if len(answers) == k:
                    return answers
        
 
        
      
        

