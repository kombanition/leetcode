class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        good_emp = 0

        for emp in hours:
            if emp >= target:
                good_emp += 1
        
        return good_emp