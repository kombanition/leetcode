class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = k % sum(chalk)        
        for i, student in enumerate(chalk):
            k -= student
            if k < 0:
                return i
       

            
        
        
