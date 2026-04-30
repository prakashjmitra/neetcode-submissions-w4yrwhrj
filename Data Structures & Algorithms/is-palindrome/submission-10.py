class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        valid_string = ""
        for letter in s:
            if letter.isalnum():
                valid_string += letter
        left = 0
        right = len(valid_string) - 1
        print(valid_string)
        while left < right:
            if valid_string[left] != valid_string[right]:
                return False
            left = left + 1
            right = right - 1
        return True

        
            