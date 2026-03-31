class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        string_list = []
        for i in range(0, len(words)):
            word = words[i]   
            for j in range(0, len(words)):
                if j == i:
                    continue
                if words[j] in words[i] and words[j] not in string_list:
                    string_list.append(words[j])
                   

        return string_list

        