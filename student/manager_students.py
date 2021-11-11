from student.student import Student


class Manager(Student):
    _managment_grade = -1
    _average_rating = -1
    _is_m = -1

    def set_manager_or_scientist_grade(self, managment):
        if managment in range(1, 6):
            self._managment_grade = managment
        else:
            print("оценка по менеджменут не корректна")
            raise Exception
    def __init__(self, age, name, surname, level, name_class, id, is_manager_or_scientist):
        Student.__init__(self, age, name, surname, level, name_class, id)
        if is_manager_or_scientist == 1:
            self._is_m = is_manager_or_scientist
        else:
            print("ошибка инициализации is_manager_or_scientist")
            raise Exception
    def get_average_rating(self):
        return round((self._managment_grade + self.get_math_grade() + self.get_russ_grade()) / 3, 3)
    def get_is_manager_or_scientist(self):
        return self._managment_grade 
    def _get_is_m(self):
        return self._is_m
    def get_iam_all(self):
        return "---> фио: " + self.get_name() + " " + self.get_surname() +\
            ", возраст: " + str(self.get_age()) + \
            ", класс: " + str(self.get_level()) + " " + self.get_name_class() +\
            ", предметы: менеджмент (" + str(self.get_is_manager_or_scientist()) + ") русский (" + str(self.get_russ_grade()) + ") математика (" + str(self.get_math_grade()) + ") средний балл (" + str(self.get_average_rating()) + ")"\
            ", отчислен: " + str(self.get_is_deducated()) + ", id: " + str(self._get_id())