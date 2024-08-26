class Solution:
    def sumZero(self, n: int) -> List[int]:
        output = []

        if n % 2 == 0:
            for i in range (0, n):
                number = -n//2 + i
                if number >= 0:
                    number += 1
                output.append(number)
        else: 
            for i in range (0, n):
                number = ceil(-n/2) + i
                output.append(number)
        return output