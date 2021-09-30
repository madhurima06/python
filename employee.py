class employee:
    def __init__(self,empid,empname,empsal,empdept):
        self.empid=empid
        self.empname=empname
        self.empsal=empsal
        self.empdept=empdept
    def display(self):
        print( self.empid,self.empname,self.empsal,self.empdept)
e=employee("20411","jack","20000","Analyst")
e.display()
