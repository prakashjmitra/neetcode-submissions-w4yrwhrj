class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        check = False
        for letter in range(len(s) -1, -1, -1):
            if s[letter].isalpha() == False and check:
                break
            if s[letter].isalpha():
                count += 1
                check = True

            
        return count
            
        