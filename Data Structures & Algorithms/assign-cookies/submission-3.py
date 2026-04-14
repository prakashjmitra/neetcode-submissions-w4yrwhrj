class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        counter = 0
        first = 0
        second = 0
        indicies = []
        g.sort()
        s.sort()
        while first <= len(g) -1:
            second = 0
            while second <= len(s) - 1:
                if s[second] >= g[first] and second not in indicies:
                    indicies.append(second)
                    counter +=1
                    break
                second += 1
            first +=1
        return counter
        