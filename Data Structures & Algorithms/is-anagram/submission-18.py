class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Brute force solution: making a hashmap of each string and checking if those two hashmaps are equal
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for n in count:
            if n != 0:
                return False
        return True
        
        
        
        



        