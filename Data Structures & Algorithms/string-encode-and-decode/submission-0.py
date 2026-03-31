class Solution:

    def encode(self, strs: List[str]) -> str:
        answer = ""
        for word in strs:
            answer = answer +  word + ";"

 
        return answer

    def decode(self, s: str) -> List[str]:
        answers = []
        blank = ""
        for letter in s:
            if letter != ";":
                blank = blank + letter
            else:
                answers.append(blank)
                blank = ""
            print(letter, blank)
        return answers
