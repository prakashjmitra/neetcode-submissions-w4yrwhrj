class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        occ = {}
        length = 0 
        l = 0
        for r in range(0, len(s),1):
            if s[r] not in occ:
                occ[s[r]] = 1
            else:
                occ[s[r]] = occ[s[r]] + 1
            # if (r-l + 1) - max(occ.values()) <= k:
            #     length = length + 1
            # else:
            #     occ[s[l]] = occ[s[l]] - 1
            #     l = l + 1
            while (r-l + 1) - max(occ.values()) > k:
                occ[s[l]] = occ[s[l]] - 1
                l = l + 1
            length = max(length,r-l + 1)
        return length
            
       

        

        