
class Director():
    _name = -1
    _surname = -1
    _average_rating = -1
    _age = -1
    _is_deducated = 0
    _id = 0
    def set_is_deducated(self, is_deducated):
        if is_deducated in range(0, 2):
            self._is_deducated = is_deducated
        else:
            print("не корректная инициализация direcor is_deducated")
    def __init__(self, name, surname, average_rating, age, id):
        if (type(name) == str) and (type(surname) == str) and \
        (type(average_rating) == float or type(average_rating) == int) and (age in range(25, 100)) and type(id) == int:
            self._name = name
            self._surname = surname
            self._average_rating = average_rating
            self._age = age
            self._id = id
        else:
            print("не корректная инициализация direcor")
            
    def get_name(self):
        return self._name
    def get_surname(self):
        return self._surname
    def get_age(self):
        return self._age
    def _get_average_rating(self):
        return self._average_rating
    def _get_is_deducated(self):
        return self._is_deducated
    def _get_id(self):
        return self._id
    
    def deduct(self, id, all_students):
        new_all_students = []
        if (type(id) == int) and (type(all_students) == list):
            for i in all_students:
                if i.get_id() == id:
                    i.set_deucate == 1
                new_all_students.append(i)
            return new_all_students
        else:
            print("некорректный ввод id студента или списка студентнов")
    def get_iam_all(self):
        return "---> фио: " + self.get_name() + " " + self.get_surname() + ", " + \
                "возраст: " + str(self.get_age()) + ", " + \
                "средний балл: " + str(self._get_average_rating()) + ", " + \
                "отчислен: " + str(self._get_is_deducated()) + ", id: " + str(self._get_id())
