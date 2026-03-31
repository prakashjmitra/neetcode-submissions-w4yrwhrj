class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        dict_A = {}
        dict_B = {}
        flag = True
        val = 0
        val2 = 0
        for i in range(0, len(s),1):
            if (s[i] in dict_A):
                dict_A[s[i]] = dict_A[s[i]] +1
            else:
                dict_A[s[i]] = 1
        for j in range(0, len(t),1):
            if (t[j] in dict_B):
                dict_B[t[j]] = dict_B[t[j]] +1
            else:
                dict_B[t[j]] = 1
            
        for k in range(0, len(s), 1):
            if s[k] not in dict_B:
                print("Reached 1")
                return False
            if (dict_A[s[k]] != dict_B[s[k]]):
                print("Reached 2")
                return False
        
        return True


        