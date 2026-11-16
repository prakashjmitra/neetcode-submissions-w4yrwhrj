class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_one = {}
        for letter in s:
            if letter in hashmap_one:
                hashmap_one[letter] += 1
            else:
                hashmap_one[letter] = 1
        hashmap_two = {}
        for letter in t:
            if letter in hashmap_two:
                hashmap_two[letter] += 1
            else:
                hashmap_two[letter] = 1
        return hashmap_one == hashmap_two