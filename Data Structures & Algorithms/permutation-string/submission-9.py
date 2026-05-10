class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        occ = defaultdict()
        for i in range(len(s1)):
            if s1[i] not in occ:
                occ[s1[i]] = 1
            else:
                occ[s1[i]] += 1
        occ2 = defaultdict()
        for j in range(len(s2)):
            if s2[j] in s1:
                for k in range(len(s1)):
                    if (j + k) < 0 or (j + k) > len(s2) -1 :
                        return False
                    if s2[j+k] not in occ2:
                        occ2[s2[j+k]] = 1
                    else:
                        occ2[s2[j+k]] += 1
                if occ == occ2:
                    return True
                else:
                    occ2 = defaultdict()
        return False
                    
            
            

        


                