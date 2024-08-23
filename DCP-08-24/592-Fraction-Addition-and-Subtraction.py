import re
from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:

        fractions = re.findall(r'[+-]?\\d+/\\d+', expression)
        real_fractions = []

        for item in fractions:
            item = Fraction(item)
            real_fractions.append(item)
        
        output = sum(real_fractions)
        
        return f\{output.numerator}/{output.denominator}\

