# Задание до 05.11

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lectorer(self, lectorer, course, grade): #метод выставления оценок лекторам
        if isinstance(lectorer, Lecturer) and course in lectorer.courses_attached :
            if course in lectorer.grades:
                lectorer.grades[course] += [grade]
            else:
                lectorer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def avr_rating(self):  # средний балл
        sum_grades = 0
        len_grades = 0
        for course in self.grades.values():  # так как курс у нас ключ в словаре
            sum_grades += sum(course)
            len_grades += len(course)
        avg_rating = round(sum_grades / len_grades, 1)
        return avg_rating

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредний балл за домашнее задание: {self.avr_rating()}\nКурсы в процессе изучения:{",".join(self.courses_in_progress)}\nЗавершенные курсы:{",".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Сравниваем только студентов со студентами и лекторов с лекторами!")
            return
        return self.avr_rating() < other.avr_rating()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avr_rating(self): #средний балл
        sum_grades = 0
        len_grades = 0
        for course in self.grades.values(): # так как курс у нас ключ в словаре
            sum_grades += sum(course)
            len_grades += len(course)
        avg_rating =round(sum_grades/len_grades,1)
        return avg_rating


    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредний балл за курс: {self.avr_rating()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Сравниваем только студентов со студентами и лекторов с лекторами!")
            return
        return self.avr_rating() < other.avr_rating()

class Reviewer(Mentor): #эксперты, проверяющие домашние задания

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
# students
best_student = Student('Ivanovich', 'Ivan', 'm')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Git']
best_student_girl = Student('Markova', 'Lidiya', 'f')
best_student_girl.courses_in_progress += ['Python']
best_student_girl.finished_courses += ['Git']
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
best_reviewer.rate_hw(best_student, 'Python', 7)
best_reviewer.rate_hw(best_student, 'Python', 4)
best_reviewer.rate_hw(best_student, 'Python', 9)

best_student.rate_lectorer(best_lectorer,'Python',87)
best_student.rate_lectorer(best_lectorer,'Python',57)

print(best_student)


# print(student1.courses_in_progress)


