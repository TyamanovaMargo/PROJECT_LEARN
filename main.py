# Задание до 05.11

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lectorer(self, lectorer, course, grade):
        if isinstance(lectorer, Lecturer) and course in lectorer.courses_attached :
            if course in lectorer.grades:
                lectorer.grades[course] += [grade]
            else:
                lectorer.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor): #эксперты, проверяющие домашние задания

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self,name,surname):
        

# students
best_student = Student('Ivanovich', 'Ivan', 'm')
best_student.courses_in_progress += ['Python']
best_student_girl = Student('Markova', 'Lidiya', 'f')
best_student_girl.courses_in_progress += ['Python']

# lectorers
best_lectorer = Lecturer('Some', 'Buddy')
best_lectorer.courses_attached += ['Python']
best_lectorer_lead = Lecturer('Burkin', 'Gleb')
best_lectorer.courses_attached += ['Python']

#reviers
best_reviewer = Reviewer('Sushkina', 'Nika')
best_reviewer.courses_attached +=['Python']
best_reviewer_teamlead = Reviewer('Korkina', 'Lida')
best_reviewer.courses_attached +=['Python']

# method
best_reviewer.rate_hw(best_student, 'Python', 10)
best_reviewer.rate_hw(best_student, 'Python', 10)
best_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_lectorer(best_lectorer,'Python',15)
best_student.rate_lectorer(best_lectorer,'Python',5)

print(best_lectorer.grades)


# print(student1.courses_in_progress)


