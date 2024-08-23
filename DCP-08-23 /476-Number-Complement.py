class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:]
        num = str(num)

        num_list = []
        output = \\

        for digit in num:
            num_list.append(digit)
        
        for digit in num_list:
            if digit == '1':
                output += '0'
            else:
                output += '1'

        return int(output, 2)
       
