from admins.director import Direcor
from student.manager_students import Manager
from student.natural_science_students import Scientist


class God(Direcor, Manager, Scientist):
    _name = "God"
    _surname = "God"
    _age = "inf"
    _surrent_director = -1
    _current_students = -1
    def set_current_director(self, director):
        if (type(director) == list):
            self._current_director = director
        else:
            print("диреткор должен быть в виде list")        