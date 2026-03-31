class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lot = set()
        l = 0
        length = 0
        for r in range(0, len(s),1):
            while s[r] in lot:
                lot.remove(s[l])
                l = l + 1
            lot.add(s[r])
            length = max(length, len(lot))
        return length
                
        
        