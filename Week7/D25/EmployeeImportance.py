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
    def getSum(self, employees: List['Employee'], id: int, total: int) ->int:
        curEmp=None
        for emp in employees:
            if(emp.id==id):
                curEmp=emp
                break
        total+=curEmp.importance
        lst=curEmp.subordinates
        for i in lst:
            total=self.getSum(employees,i,total)
        return total        
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        return self.getSum(employees,id,0)
    
