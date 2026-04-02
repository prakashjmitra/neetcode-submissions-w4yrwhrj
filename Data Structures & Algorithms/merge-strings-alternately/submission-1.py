class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_i = 0
        word2_i = 0
        answer = ""
        while word1_i <= len(word1) -1 or word2_i <= len(word2) -1:
            if word1_i <= len(word1) -1:
                answer += word1[word1_i]
                word1_i += 1
            if word2_i <= len(word2) -1 :
                answer += word2[word2_i]
                word2_i += 1
        return answer
