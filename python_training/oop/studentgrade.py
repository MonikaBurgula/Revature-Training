#from StudDetail import StudentDetail
#from functions.avg import student_name
from oop.TeacherDetails import TeacherDetails
from studexcurr import StudExCurr
from TeacherDetails import TeacherDetails
from finaleval import FinalEval

ccode = input('Enter ccode: ')
cname = input('Enter name: ')

rollno = int(input('Enter roll no: '))
sname = input('Enter name: ')
m1 = int(input('mark 1: '))
m2 = int(input('mark 2: '))
m3 = int(input('mark 3: '))
exm1 = int(input('Ex mark 1: '))
exm2 = int(input('Ex mark 2: '))

 #StudentDetail(ccode, cname, rollno, name, m1, m2, m3)

'''stud = StudExCurr(ccode, cname, rollno, sname, m1, m2, m3, exm1, exm2)
print(f'{stud.display()[0]} \t {stud.display()[1]} \t ')
print(f'{stud.get_rollno()}\n {stud.sname}\n '
      f'{stud.calc_tot()}\n '
      f'{stud.calc_avg()}')
print(f'{stud.calc_extot()}')'''

empid = int(input('Enter empid: '))
tname = input('Enter tname: ')
dept = input('Enter dept: ')

'''teacher = TeacherDetails(ccode, cname, empid, tname, dept)
teacher.display()'''

feedbackfromteacher = input('Enter feedback: ')

finaleval = FinalEval (ccode, cname, rollno, sname, m1, m2, m3, exm1, exm2, empid, tname, dept, feedbackfromteacher)

finaleval.coll_display()
print(f'{finaleval.get_rollno()}\n {finaleval.sname}\n '
      f'{finaleval.calc_tot()}\n '
      f'{finaleval.calc_avg()}\n '
      f'{finaleval.calc_extot()}\n ')

finaleval.teachers_display()
print(f'{finaleval.feedbackfromteacher}')
