class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Brute force solution: making a hashmap of each string and checking if those two hashmaps are equal
        s_map = defaultdict()
        t_map = defaultdict()
        for letter in s:
            if letter in s_map:
                s_map[letter] += 1
            else:
                s_map[letter] = 1
        for letter in t:
            if letter in t_map:
                t_map[letter] += 1
            else:
                t_map[letter] = 1
        return s_map == t_map
        
        
        
        



        