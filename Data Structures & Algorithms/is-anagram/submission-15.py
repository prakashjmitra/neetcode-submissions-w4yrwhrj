class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Brute force solution: making a hashmap of each string and checking if those two hashmaps are equal
        string1 = sorted(s)
        string2 = sorted(t)
        return string1 == string2
        
        
        



        