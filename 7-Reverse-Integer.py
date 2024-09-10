class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        output = []
        for digit in str(x):
            if digit == '-':
                neg = True
            else:
                output.append(digit)
        output = int(\\.join(output[::-1]))

        if neg and -2**31 < output < 2**31-1:
            return output * -1
        elif -2**31 < output < 2**31-1:
            return output
        else:
            return 0