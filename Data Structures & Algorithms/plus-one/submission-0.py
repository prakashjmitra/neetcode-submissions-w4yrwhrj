class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        counter = 0
        for i in range(len(digits) -1, -1, -1):
            number += digits[i] * (10** counter)
            counter += 1
        number += 1
        snum = str(number)
        answer = []
        for letter in snum:
            answer.append(int(letter))
        return answer

