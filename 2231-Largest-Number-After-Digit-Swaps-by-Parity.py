class Solution:
    def largestInteger(self, num: int) -> int:
        num = list(str(num))
        odd = []
        even = []
        output = []

        for digit in num:
            if int(digit) % 2 == 0:
                even.append(digit)
            else: 
                odd.append(digit)
        
        for digit in num:
            if  int(digit) % 2 == 0:
                output.append(max(even))
                even.remove(max(even))
            if  int(digit) % 2 != 0:
                output.append(max(odd))
                odd.remove(max(odd))

        return int("".join(output))        