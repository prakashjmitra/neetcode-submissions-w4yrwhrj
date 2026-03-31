class Solution:

    def encode(self, strs: List[str]) -> str:
        answer = ""
        for word in strs:
            answer = answer + str(len(word)) + ";" + word

 
        return answer

    def decode(self, s: str) -> List[str]:
        answers = []
        i = 0
        while i < len(s):
            j = i
            while str(s[j]) != ";":
                j = j + 1
            length = int(s[i:j])
            answers.append(s[j+1:j+1+length])
            i = j + 1 + length
        return answers

        
