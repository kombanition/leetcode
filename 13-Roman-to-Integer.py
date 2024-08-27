class Solution:
    def romanToInt(self, s: str) -> int:

        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        prev_value = 0
        total = 0

        for char in s:
            if roman_map[char] > prev_value:
                total += roman_map[char] - 2 * prev_value
                prev_value = roman_map[char]
            else:
                total += roman_map[char]
                prev_value = roman_map[char]
    
        return total
        
