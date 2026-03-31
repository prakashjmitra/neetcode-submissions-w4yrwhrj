class Solution:

    def encode(self, strs: List[str]) -> str:
        answer = ""
        for string in strs:
            answer += string
            answer += "á"
        print(answer)
        return answer
        

    def decode(self, s: str) -> List[str]:
        strings = []
        word = ""
        for char in s:
            print("Here")
            if char != "á":
                word += char
            else:
                print("Reached")
                strings.append(word)
                word = ""
        return strings
        

        
