from abc import abstractmethod


class Student(object):
    _id = -1
    _math_grade = -1
    _russ_grade = -1
    _age = -1
    _name = -1
    _surname = -1
    _level = -1
    _name_class = -1
    _is_deducted = 0
    _is_dir = 0
    def set_is_dir(self, is_dir):
        if is_dir in range(0, 2):
            self._is_dir = is_dir
        else:
            print("is_dir не корректна")
            raise Exception
    def set_math_grade(self, math):
        if (type(math) == int) and (math in range(1, 6)):
            self._math_grade = math
        else:
            print("оценка по матиматике не корректна")
            raise Exception
    def set_russ_grade(self, russ):
        if (type(russ) == int) and (russ in range(1, 6)):
            self._russ_grade = russ
        else:
            print("оценка по русскому не корректна")
            raise Exception
    def set_deucate(self, deducate):
        if deducate == 0 or deducate == 1:
            self._is_deducted = deducate
        else:
            print("ввод кода отчисления не корректен")
            raise Exception
    def __init__(self, age, name, surname, level, name_class, id):
        if (type(name) == str) and (type(surname) == str) \
        and (name_class in "AB") and (age in range(6, 19)) \
        and (level in range(6, 12)) and (type(id) == int):
            self._id = id
            self._age = age
            self._name = name
            self._surname = surname
            self._level = level
            self._name_class = name_class
        else:
            print("данные студента не корректны")
            raise Exception
    @abstractmethod
    def get_average_rating(self):
        pass   
    def get_math_grade(self):
        return self._math_grade  
    def get_russ_grade(self):
        return self._russ_grade
    def get_name(self):
        return self._name
    def get_level(self):
        return self._level
    def get_name_class(self):
        return self._name_class
    def get_surname(self):
        return self._surname
    def get_age(self):
        return self._age
    def _get_id(self):
        return self._id
    def get_is_deducated(self):
        return self._is_deducted
    def get_is_dir(self):
        return self._is_dir


