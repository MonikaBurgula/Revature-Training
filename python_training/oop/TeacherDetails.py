from oop.College import College

class TeacherDetails(College):
    def __init__(self,ccode, cname, empid, tname, dept):
        College.__init__(self, ccode, cname)
        self.empid = empid
        self.tname = tname
        self.dept = dept

    def teachers_display(self):
        print(f'{self._ccode}\t {self._cname}\n'
              f'{self.empid}\n {self.tname}\n {self.dept}')
