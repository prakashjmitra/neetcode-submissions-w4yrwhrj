class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            thing = s[:i] + s[i+1:]
            if self.checkPalindrome(thing):
                return True
            word = s
        return False

    
    def checkPalindrome(self, word: str) -> bool:
        left = 0
        right = len(word) -1
        while left < right:
            if word[left] != word[right]:
                return False
            left = left + 1
            right = right - 1
        return True
            
        