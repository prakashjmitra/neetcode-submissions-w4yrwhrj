class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        first = 0
        second = 0
        g.sort()
        s.sort()

        while first <= len(g) -1:
            while second <= len(s) -1 and g[first] > s[second]:
                second +=1
            if second <= len(s) -1:
                first += 1
                second +=1 
            else:
                break
                
             
            
        return first
        