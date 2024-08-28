class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        n = 0
        isP = False

        for item in x:
            if item == x[len(x) - (1 + n)]:
                isP = True
            else: 
                isP = False
                break
            n += 1
        
        return isP