class Solution:
    def getLucky(self, s: str, k: int) -> int:
        output = []
        
        if len(s) == 1 and ord(s.upper()) - ord("A") + 1 < 10:
            return ord(s.upper()) - ord("A") + 1

        for letter in s:
            
            output.append(str(ord(letter.upper()) - ord("A") + 1))
        output = "".join(output)

        while int(output) > 9 and k != 0:
            k -= 1
            output = sum(int(digit) for digit in str(output))

        return output