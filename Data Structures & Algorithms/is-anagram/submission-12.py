class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = defaultdict(int)
        for letter in s:
            if letter not in s:
                hashmap[letter] = 1
            else:
                hashmap[letter] += 1
        
        anothermap = defaultdict(int)
        for l in t:
            if l not in t:
                anothermap[l] = 1
            else:
                anothermap[l] += 1
        return hashmap == anothermap
        
        
        



        