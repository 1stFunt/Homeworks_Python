# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
import csv


class NameDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not value.isalpha() or not value[0].isupper():
            raise ValueError("ФИО должно содержать только буквы и начинаться с заглавной буквы")
        instance.__dict__[self.name] = value

class Student:
    first_name = NameDescriptor("first_name")
    last_name = NameDescriptor("last_name")
    middle_name = NameDescriptor("middle_name")

    def __init__(self, first_name, last_name, middle_name, subjects_file):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        # Загрузка названий предметов из CSV-файла
        with open(subjects_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            # Предполагается, что названия предметов записаны в первой строке файла
            self.subjects = list(reader)[0]
        # Инициализация словаря для хранения оценок и результатов тестов
        self.grades = {subject: {'grades': [], 'test_results': []}
                       for subject in self.subjects}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError("Недопустимый предмет")
        if grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть от 2 до 5")
        self.grades[subject]['grades'].append(grade)

    def add_test_result(self, subject, test_result):
        if subject not in self.subjects:
            raise ValueError("Недопустимый предмет")
        if test_result < 0 or test_result > 100:
            raise ValueError("Результат теста должен быть от 0 до 100")
        self.grades[subject]['test_results'].append(test_result)

    def average_grade(self, subject):
        if subject not in self.subjects:
            raise ValueError("Недопустимый предмет")
        grades = self.grades[subject]['grades']
        if not grades:
            return None
        return sum(grades) / len(grades)

    def average_test_result(self, subject):
        if subject not in self.subjects:
            raise ValueError("Недопустимый предмет")
        test_results = self.grades[subject]['test_results']
        if not test_results:
            return None
        return sum(test_results) / len(test_results)

    def overall_average_grade(self):
        all_grades = [grade for subject_data in self.grades.values()
                      for grade in subject_data['grades']]
        if not all_grades:
            return None
        return sum(all_grades) / len(all_grades)

    def subject_average_grade(self):
        subject_averages = {}
        for subject, data in self.grades.items():
            grades = data['grades']
            if grades:
                subject_averages[subject] = sum(grades) / len(grades)
        return subject_averages

    def subject_average_test_result(self):
        subject_averages = {}
        for subject, data in self.grades.items():
            test_results = data['test_results']
            if test_results:
                subject_averages[subject] = sum(
                    test_results) / len(test_results)
        return subject_averages


# Пример использования:
student = Student("Иван", "Иванов", "Иванович", "subjects.csv")
# Добавление оценок и результатов тестов для Математики
student.add_grade("Математика", 4)
student.add_test_result("Математика", 80)
student.add_grade("Математика", 5)
student.add_test_result("Математика", 90)
# Добавление оценок и результатов тестов для Физики
student.add_grade("Физика", 4)
student.add_test_result("Физика", 85)
student.add_grade("Физика", 5)
student.add_test_result("Физика", 95)
# Добавление оценок и результатов тестов для Химии
student.add_grade("Химия", 3)
student.add_test_result("Химия", 70)
student.add_grade("Химия", 4)
student.add_test_result("Химия", 75)
# Вычисление и вывод средних результатов тестов по всем предметам
print("Средний результат тестов по каждому предмету:",
      student.subject_average_test_result())
# Вычисление и вывод средних баллов по всем предметам
print("Средний балл по оценкам по каждому предмету:",
      student.subject_average_grade())
# Вычисление и вывод общего среднего балла
print("Общий средний балл по всем предметам:", student.overall_average_grade())