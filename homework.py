from statistics import median

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course].append(grade)
            else:
                lector.grades[course] = [grade]
        else:
            return 'Error'

    def avg_rate(self, course):
        if course in self.grades:
            avg_r = median(self.grades[course])
            return avg_r
        return 0

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.avg_rate}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_lecture_rate(self, course):
        if course in self.grades:
            return median(self.grades[course])
        return 0

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекцию: {self.avg_lecture_rate}')

class Rewiewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'male')
worst_student = Student('Vasilisa', 'Pupkina', 'female')
best_student.courses_in_progress += ['Python', 'JavaScript']
worst_student.courses_in_progress += ['Python', 'Java']



fn_reviewer = Rewiewer('Ya', 'Chumba')
fn_reviewer.courses_attached += ['Python', 'JavaScript']

sd_reviewer = Rewiewer('Dzen', 'Chumba')
sd_reviewer.courses_attached += ['Python', 'Java']


fn_lector = Lecturer('Basha', 'Buzuki')
fn_lector.courses_attached += ['Python', 'JavaScript']
sd_lector = Lecturer('Sam', 'Huang')
sd_lector.courses_attached += ['Python', 'Java']


fn_reviewer.rate_hw(best_student, 'Python', 9)
fn_reviewer.rate_hw(worst_student, 'Java', 8)
sd_reviewer.rate_hw(best_student, 'JavaScript', 10)
sd_reviewer.rate_hw(worst_student, 'Python', 9)

best_student.rate_lecture(fn_lector, 'Python', 9)
best_student.rate_lecture(fn_lector, 'JavaScript', 8)
worst_student.rate_lecture(fn_lector, 'Python', 10)
worst_student.rate_lecture(sd_lector, 'Java', 9)


print(fn_lector.avg_lecture_rate('Python'))