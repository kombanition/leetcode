class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = str(format(start, 'b'))
        goal = str(format(goal, 'b'))
        max_len = max(len(start), len(goal))
        start = start.zfill(max_len)
        goal = goal.zfill(max_len)
        output = 0

           
        for s, g in zip(start, goal):
            if s != g:
                output += 1      
        return output
        