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
                lector.grades[course] += grade
            else:
                lector.grades[course] = grade
        else:
            return 'Error'

    def avg_rate(self, course):
        avg_r = median(self.grades[course])
        return avg_r

    def __str__(self):
        print(f'Имя{self.name}\nФамилия{self.surname}\nСредняя оценка за домашние задания:{self.avg_rate}\n'
              f'Курсы в процессе изучения:{self.courses_in_progress}\nЗавершенные курсы:{self.finished_courses}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        print(f'Имя:{self.name}\nФамилия:{self.surname}\n"Средняя оценка за лекцию"{self.grades}')


class Rewiewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print(f'Имя:{self.name}\nФамилия:{self.surname}')
