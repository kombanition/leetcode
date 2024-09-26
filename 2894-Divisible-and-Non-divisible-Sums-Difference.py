class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = []
        num2 = []

        for number in range(1, n + 1):
            if number % m != 0:
                num1.append(number)
            else:
                num2.append(number)
        
        return sum(num1) - sum(num2)