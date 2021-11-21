import School;
import Teacher;
import Student;

school1 = School.School("School 1", "location 1", "Person in charge 1")
school2 = School.School("School 2", "location 2", "Person in charge 2")
teacher1 = Teacher.Teacher("Teacher 1", "Math", school1)
student1 =  Student.Student("Student 1", "CSE", teacher1, school1);
print(student1.teacher.name)