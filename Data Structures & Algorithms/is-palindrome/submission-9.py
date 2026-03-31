class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        first = 0
        last = len(s) - 1
        while first < last:
            if s[first] != s[last]:
                print(s[first], s[last])
                return False
            first = first + 1
            last = last - 1
        return True
        
            