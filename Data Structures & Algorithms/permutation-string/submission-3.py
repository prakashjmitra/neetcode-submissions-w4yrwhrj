class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        for r in range(len(str(s1)), len(s2)+1,1):
            print(l,r)
            print(s2[l:r])
            if sorted(s1) == sorted(s2[l:r]):
                return True
            l = l+1
        return False


                