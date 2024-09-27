class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        for number1 in range(1, n):
            number2 = n - number1
            if number1 + number2 == n and "0" not in str(number1) and "0" not in str(number2):
                return number1 , number2 