class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t) or len(t) > len(s):
            return False
        matches = defaultdict(int)
        matches2 = defaultdict(int)
        for i in range(len(t)):
            if t[i] not in s: 
                return False
            else:
                matches[t[i]] += 1
        for j in range(len(s)):
            if s[j] not in t: 
                return False
            else:
                matches2[s[j]] += 1
        # for a in matches:
        #     print(a, matches[a])
        # for b in matches2:
        #     print(b, matches2[b])
        return matches == matches2
            
        



        
        return True
        



        