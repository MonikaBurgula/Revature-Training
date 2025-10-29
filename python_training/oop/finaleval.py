from studexcurr import StudExCurr
from TeacherDetails import TeacherDetails


class FinalEval(StudExCurr, TeacherDetails):
    def __init__(self, ccode, cname, rollno, sname, m1, m2, m3, exm1, exm2,
                 empid, tname, dept, feedbackfromteacher):

        StudExCurr.__init__(self, ccode, cname, rollno, sname, m1, m2, m3, exm1, exm2)
        TeacherDetails.__init__(self, ccode, cname, empid, tname, dept)
        self.feedbackfromteacher = feedbackfromteacher
