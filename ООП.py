class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.student_assessment = {}

    def teaching_assessment(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course and lecturer.courses_attached:
            if course in lecturer.student_assessment:
                lecturer.student_assessment[course] += [grade]
            else:
                lecturer.student_assessment[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self, grade):
        average_rating = []
        courses = []
        for key, value in self.grades.items():
            average_rating += value
            if key not in courses:
                courses.append(key)
            else:
                courses += key
        mean = round((sum(average_rating) / len(average_rating)), 1)
        if grade == 'grade':
            return mean
        elif grade == 'list courses':
            return courses

    def __str__(self):
        grade = 'grade'
        list_courses_with_grade = 'list courses'
        res = (f"\nИмя: {self.name}"
        f"\nФамилия: {self.surname}"
        f"\nСредняя оценка за домашние задания: {self._average_rating(grade)}"
        f"\nКурсы в процессе изучения: {', '.join(self._average_rating(list_courses_with_grade))}"
        f"\nЗавершенные курсы:{', '.join(self.finished_courses)}")
        return res

    def __lt__(self, other):
        grade = 'grade'
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self._average_rating(grade) < other.average_feedback()

    def __gt__(self, other):
        grade = 'grade'
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self._average_rating(grade) > other.average_feedback()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname, lecturer):
        super().__init__(name, surname, lecturer)
        self.student_feedback = {}
        self.student_assessment = {}


    def average_feedback(self):
        average_feedback_list = []
        for key, value in self.student_feedback.items():
            average_feedback_list += value
        mean = round((sum(average_feedback_list) / len(average_feedback_list)), 1)
        return mean

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_feedback()}'
        return res


class Reviewer(Mentor):
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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


    def average_student_grade(course, *students):
        """
        Подсчитываем среднюю оценку всех студентов в рамках конкретного курса"""
        list_st = []
        for student in students:
            if students.grades.get(course):
                list_st.extend(student.grades[course])
        return round(sum(list_st) / len(list_st), 1)


    def average_feedback_lectures(course, *lectures):
        """
        Подсчитываем среднюю оценку всех лекторов в рамках конкретного курса"""
        list_st = []
        for lecturer in lectures:
            if lecturer.student_feedback(course):
                list_st.extend(lecturer.student_feedback[course])
        return round(sum(list_st) / len(list_st), 1)


academically_successful_student_1 = Student('Name_student_1', 'Surname_student_1', 'your_gender')
academically_successful_student_2 = Student('Name_student_2', 'Surname_student_2', 'your_gender')

academically_successful_student_1.courses_in_progress += ['Python']
academically_successful_student_2.courses_in_progress += ['Python']
academically_successful_student_1.courses_in_progress += ['GIT']
academically_successful_student_2.courses_in_progress += ['GIT']

academically_successful_student_1.finished_courses += ['Введение в программирование']
academically_successful_student_1.finished_courses += ['Введение в программирование']

homework_check_1 = Reviewer("Name_reviewer_1", "Surname_reviewer_1")
homework_check_2 = Reviewer("Name_reviewer_2", "Surname_reviewer_2")

homework_check_1.courses_attached += ['Python']
homework_check_1.courses_attached += ['GIT']
homework_check_2.courses_attached += ['Python']
homework_check_2.courses_attached += ['GIT']

homework_check_1.rate_hw(academically_successful_student_1, 'Python', 10)
homework_check_1.rate_hw(academically_successful_student_1, 'Python', 7)
homework_check_2.rate_hw(academically_successful_student_2, 'Python', 10)
homework_check_2.rate_hw(academically_successful_student_2, 'Python', 5)
homework_check_1.rate_hw(academically_successful_student_1, 'GIT', 10)
homework_check_1.rate_hw(academically_successful_student_1, 'GIT', 9)
homework_check_2.rate_hw(academically_successful_student_2, 'GIT', 10)
homework_check_2.rate_hw(academically_successful_student_2, 'GIT', 8)

lector_course_1 = Lecturer('Name_lecturer_1', 'Surname_lecturer_1')
lector_course_2 = Lecturer('Name_lecturer_2', 'Surname_lecturer_2')

lector_course_1.courses_attached += ['Python']
lector_course_1.courses_attached += ['GIT']
lector_course_2.courses_attached += ['Python']
lector_course_2.courses_attached += ['GIT']


academically_successful_student_1.teaching_assessment(lector_course_1, "Python", 10)
academically_successful_student_2.teaching_assessment(lector_course_1, "Python", 8)
academically_successful_student_1.teaching_assessment(lector_course_1, "GIT", 6)
academically_successful_student_1.teaching_assessment(lector_course_1, "Python", 7)
academically_successful_student_2.teaching_assessment(lector_course_2, "Python", 5)
academically_successful_student_1.teaching_assessment(lector_course_2, "GIT", 7)
academically_successful_student_1.teaching_assessment(lector_course_2, "Python", 8)
academically_successful_student_2.teaching_assessment(lector_course_2, "GIT", 9)


print(f"{'=' * 80}\n'Задание № 2.'")
print(f"\n{academically_successful_student_1.grades}")
print(f"\n{lector_course_1.student_feedback}")
print(f"\n{'=' * 80}\n'Задание № 3.'")
print(f"\n{homework_check_1}")
print(f"\n{lector_course_1}")
print(f"\n{academically_successful_student_1}")

print(academically_successful_student_1 < lector_course_1)
print(academically_successful_student_1 > lector_course_1)

print(f"\n{'=' * 80}\n'Задание № 4.'")
course = "GIT"
print(average_student_grade(course, academically_successful_student_1, academically_successful_student_2))
print(average_feedback_lectures(course, lector_course_1, lector_course_2))




