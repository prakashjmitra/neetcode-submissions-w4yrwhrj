class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        for letter in s:
            if letter in first:
                first[letter] += 1
            else:
                first[letter] = 1
        second = {}
        for thing in t:
            if thing in second:
                second[thing] += 1
            else:
                second[thing] = 1
        return first == second
        
        
        



        