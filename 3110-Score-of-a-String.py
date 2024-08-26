class Solution:
    def scoreOfString(self, s: str) -> int:
        s = list(s)
        output = []
        
        for i in range(0, len(s) - 1):
            output.append(abs(ord(s[i]) - ord(s[i+ 1])))
        
        return sum(output)