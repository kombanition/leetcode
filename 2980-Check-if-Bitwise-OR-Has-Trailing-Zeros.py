class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool: 
        count = 0
        for number in nums:
            if bin(number)[2:][-1] == '0':
                count += 1      
        if count >= 2:
            return True
        else:
            return False