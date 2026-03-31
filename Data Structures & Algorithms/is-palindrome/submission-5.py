class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.replace(" ","")
        string = string.lower()
        one = 0
        two = len(string) -1
        if len(string) == 1 or len(string) == 0:
            return True
        if len(string) == 2:
            if not(string[0].isalnum()) or not(string[1].isalnum()):
                return True
            return string[0] == string[1]
        for k in range(len(string)):
            if two < one:
                return True
            if not(string[one].isalnum()):
                one = one + 1
                continue
            if not(string[two].isalnum()):
                two = two - 1
                continue

            if string[one] != string[two]:
                print(string[one])
                print(string[two])
                return False
            one = one + 1
            two = two -1
        
        return True