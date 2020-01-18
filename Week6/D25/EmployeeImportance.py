"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getSum(self,employees: List['Employee'], id: int,s: List[int]) -> int:
        for emp in employees:
            if(emp.id==id):
                currEmployee=emp
        curr=currEmployee.importance
        s.append(curr)
        lst=currEmployee.subordinates
        for empId in lst:
            self.getSum(employees,empId,s)
        return s
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        lst=[]
        lst=self.getSum(employees,id,lst)
        return sum(lst)
