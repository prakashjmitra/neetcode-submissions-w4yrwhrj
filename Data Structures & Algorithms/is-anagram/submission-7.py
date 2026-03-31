class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}
        for a in range(len(s)):
            if s[a] not in first:
                first[s[a]] = 1
            else:
                first[s[a]] += 1
        for b in range(len(t)):
            if t[b] not in second:
                second[t[b]] = 1
            else:
                second[t[b]] += 1
        return first == second
        

        