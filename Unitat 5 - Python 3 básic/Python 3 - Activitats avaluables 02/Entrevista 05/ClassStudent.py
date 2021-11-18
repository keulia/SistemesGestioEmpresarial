

class Student:
    def __init__(self, name, grade, tutor):
        self.name = name
        self.grade = grade
        tutor.returnTeacher = tutor #IM SURE THIS is wrong 

    def returnStudent(self):
        return self.name
        return self.grade
        return self.tutor