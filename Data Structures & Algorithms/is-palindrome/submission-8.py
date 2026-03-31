class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        last = len(s) - 1
        s = s.lower()
        while first < last:
            print(first,last)
            
            while first < last and not(s[first].isalnum()):
                first = first + 1
            while first  < last and not(s[last].isalnum()):
                last = last - 1
            if s[first] != s[last]:
                print(s[first],s[last])
                return False
            first = first + 1
            last = last - 1
        return True