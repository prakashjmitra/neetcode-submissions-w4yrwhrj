class Solution:
    def minWindow(self, s: str, t: str) -> str:
        occ = defaultdict()
        candidates = []
        counter = 0
        for letter in t:
            if letter not in occ:
                occ[letter] = 1
            else:
                occ[letter] += 1
        for i in range(len(s)):
            occ2 = defaultdict()
            string = ""
            
            flag = False
            dont2 = False
            if s[i] in t:
                z = i
                while z <= len(s) - 1:
                    if s[z] not in occ2:
                        occ2[s[z]] = 1
                    else:
                        occ2[s[z]] += 1
                    string += s[z]
                    z += 1
                    dont = False
                    for key in occ:
                        if key not in occ2 or occ[key] > occ2[key]:
                            dont = True
                    if not dont:
                        print('reached')
                        flag = True
                    if flag:
                        print('reached')
                        break

                if string == t:
                    return string
          
                print(string)
                for key in occ:
                    if key not in occ2 or occ[key] > occ2[key]:
                        
                        dont2 = True
                if not dont2:
                    candidates.append(string)
                

        for word in candidates:
            pass
            # print(word)
        if len(candidates) == 0:
            return ""
        return min(candidates, key = len)
        

                     

