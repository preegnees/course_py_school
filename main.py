import random
from student.manager_students import Manager
from student.natural_science_students import Scientist
from admins.director import Director
from russian_names import RussianNames

root = 1
director = 2
student = 3

director_list_one = []
students_list = []
deleted_studets_list = []
root_list_one = []
docs_of_deleted_students = []

count_students = 10
count_director = 1


def generate_students(count):
    for _ in range(0, count):
        is_scientist_or_manager =  random.randint(1,2)
        full_name = RussianNames(count=1, patronymic=False, transliterate=False).get_batch()
        age = random.randint(6, 18)
        name = full_name[0].split(" ")[0]
        surname = full_name[0].split(" ")[1]
        level = random.randint(6, 11)
        name_class = str(chr(random.randint(ord("A"), ord("B")))).upper()
        id = random.randint(1, 10000000)
        if is_scientist_or_manager == 1:
            new_stident = Manager(age=age, name=name, surname=surname, level=level, name_class=name_class, id=id, is_manager_or_scientist=is_scientist_or_manager)
            students_list.append(new_stident)
        else:
            new_stident = Scientist(age=age, name=name, surname=surname, level=level, name_class=name_class, id=id, is_manager_or_scientist=is_scientist_or_manager)
            students_list.append(new_stident)
    return students_list[0]
def generate_director():
    full_name = RussianNames(count=1, patronymic=False, transliterate=False).get_batch()
    name = full_name[0].split(" ")[0]
    surname = full_name[0].split(" ")[1]
    average_rating = round(random.uniform(3, 5), 3)
    age = random.randint(26, 99)
    id = random.randint(1, 10000000)
    new_director = Director(age=age, name=name, surname=surname, average_rating=average_rating, id=id)
    director_list_one.insert(0, new_director)
    for i in director_list_one:
        if i == new_director:
            continue
        i.set_is_deducated(1)
    return director_list_one[0]

def test_for_students():
    for i in students_list:
        russ = random.randint(2, 5)
        math = random.randint(2, 5)
        other = random.randint(2, 5)
        i.set_math_grade(math)
        i.set_russ_grade(russ)
        i.set_manager_or_scientist_grade(other)
################################################################################################
def is_root(inp):
    if inp == 1:
        
        inp_one = ""
        while inp_one != "q":
            print("посмотреть всех студентов [1],\n" \
                "сортировка по среднему баллу [2],\n" \
                "посмотреть отчисленных студентов [3],\n" \
                "изменить студента [4],\n" \
                "исключить студента студента [5],\n" \
                "посмотреть заявления [6],\n" \
                "поставить студента на место дургого [7],\n" \
                "помиловать студента заявления [8],\n" \
                "провести контрольную работу [9].\n" \
                "назад [q]\n")
            i = input()
            if i == "q":
                break
            try:
                i = int(i)
            except:
                continue
            if i == 1:
                all_stud = students_list + deleted_studets_list
                for i in all_stud:
                    print(i.get_iam_all())
            if i == 2:
                all_stud = students_list + deleted_studets_list
                all_stud.sort(key=lambda x: x.get_average_rating(), reverse=True)
                for i in all_stud:
                    print(i.get_iam_all())
            if i == 3:
                for i in deleted_studets_list:
                    print(i.get_iam_all())
            if i == 4:
                all_stud = students_list + deleted_studets_list
                print("введите id студента, которого хотите изменить, назад [q]")
                id_str = input()
                if id_str == "q":
                    continue
                else:
                    id_str = int(id_str)
                curr_std = 0
                for i in all_stud:
                    if id_str == i._get_id():
                        curr_std = i
                print("ваш кандидат")
                print(curr_std.get_iam_all())
                print("введите возраст")
                a = int(input())
                curr_std._age = a
                print("введите имя")
                n = input()
                curr_std._name = n
                print("введите фамилию")
                s = input()
                curr_std._surname = s
                print("введите цифру класса")
                cl_n = int(input())
                curr_std._level = cl_n
                print("введите букву класса")
                cl_name = input()
                curr_std._name_class = cl_name
                print("введите id")
                id = int(input())
                curr_std._id = id
                print("введите направление: менеджер - 1, физик - 2")
                other = int(input())
                curr_std.set_manager_or_scientist_grade = other
                print("будет отличленным, нет - 0, да - 1")
                d = int(input())
                if d == 1:
                    curr_std._is_deducted = d
                    deleted_studets_list.append(curr_std)
                    students_list.remove(curr_std)
                else:
                    curr_std._is_deducted = 0
                print(curr_std.get_iam_all())
                
            if i == 5:
                print("введи id студента, назад [q]")
                id_inp = input()
                if id_inp == "q":
                    return
                try:
                    id = int(id_inp)
                except:
                    return
                for i in students_list:
                    if id == i._get_id():
                        i.set_deucate(1)
                        deleted_studets_list.append(i)
                        students_list.remove(i)
            if i == 6:
                print("заявления: ")
                for i in docs_of_deleted_students:
                    print(i)
            if i == 7:
                all_stud = students_list + deleted_studets_list
                print("введи id двух студентов через пробел для переноса (1-->2), назад [q]")
                id_inp = input()
                if id_inp == "q":
                    return
                try:
                    id_1 = int(id_inp.split(" ")[0])
                    id_2 = int(id_inp.split(" ")[1])
                except:
                    return
                curr_one = 0
                curr_two = 0
                for i in all_stud:
                    if id_1 == i._get_id():
                        curr_one = i
                    if id_2 == i._get_id():
                        curr_two = i
                curr_two._id = curr_one._id
                curr_two._math_grade = curr_one._math_grade
                curr_two._russ_grade = curr_one._russ_grade
                curr_two._age = curr_one._age
                curr_two._name = curr_one._name
                curr_two._surname = curr_one._surname
                curr_two._level = curr_one._level
                curr_two._name_class = curr_one._name_class
                curr_two._is_deducted = curr_one._is_deducted
                curr_two._average_rating = curr_one._average_rating
                for i in all_stud:
                    if id_1 == i._get_id():
                        curr_one = i
                        break

            if i == 8:
                print("введи id студента, назад [q]")
                id_inp = input()
                if id_inp == "q":
                    return
                try:
                    id = int(id_inp)
                except:
                    return
                for i in deleted_studets_list:
                    if id == i._get_id():
                        i.set_deucate(0)
                        students_list.append(i)
                        deleted_studets_list.remove(i)
            if i == 9:
                test_for_students()






                
    if inp == 2:
        inp_two = ""
        while inp_two != "q":
            new_dir = director_list_one[0]
            print("посмотреть текущего директора [1],\n" \
                "посмотреть всех директоров [2],\n" \
                "сменить директора [3],\n" \
                "сменить данные директора [4],\n" \
                "назад [q]\n")
            i = input()
            if i == "q":
                break
            try:
                i = int(i)
            except:
                continue
            if i == 1:
                print(new_dir.get_iam_all())
            if i == 2:
                for i in director_list_one:
                    print(i.get_iam_all())
            if i == 3:
                generate_director()
            if i == 4:
                print("введите буквенное имя:")
                n = input()
                new_dir._name = n
                print("введите буквенную фамилию:")
                s = input()
                new_dir._surname = s
                print("введите возраст:")
                a = input()
                new_dir._age = a
                print("введите средний рейтинг, в виде: \"2.234\":")
                r = float(input())
                new_dir._average_rating = r
                print("хотите его отчислить, на замену прийдет новй: 0 - нет, 1 - да")
                d = int(input())
                if d == 1:
                    generate_director()
                else:
                    d = 0
                new_dir._is_deducated = d

    if inp == 3:
        print("     X           X                X           X")
        print("       X       X                    X       X  ")
        print("         X   X                        X   X    ")
        print("           X                            X      ")
        print("         X   X                        X   X    ")
        print("       X       X                    X       X  ")
        print("     X           X                X           X")
        print("                                               ")
        print("                                               ")
        print("                   --------------              ")
   
        raise Exception
###############################################################################################

def is_director(inp, dir, iam):
    if inp == 1:
        print(dir.get_iam_all())
        print("")
    if inp == 2:
        for i in students_list:
            print(i.get_iam_all())
            print("")
    if inp == 3:
        generate_director()
    if inp == 4:
        print("введи id студента, назад [q]")
        id_inp = input()
        if id_inp == "q":
            return
        try:
            id = int(id_inp)
        except:
            return
        for i in students_list:
            if id == i._get_id():
                i.set_deucate(1)
                deleted_studets_list.append(i)
                students_list.remove(i)
    if inp == 5:
        test_for_students()

def is_student(inp, iam):
    is_d = iam.get_is_deducated()
    if inp == 3 or is_d == 1 :
            print("Подать заявление [1], назад [q]")
            appelation = input()
            if appelation == "q":
                return
            try:
                if int(appelation) == 1:
                    print("напиши заявление")
            except:
                return
            doc = str(input())
            a = "id: " + str(iam._get_id()) + ", message: " + doc 
            docs_of_deleted_students.append(a)
            if is_d == 1:
                return
    if inp == 1:
        print(iam.get_iam_all())
        print("")
    if inp == 2:
        cur_class = iam.get_name_class() + str(iam.get_level())
        cur_id = iam._get_id()
        for i in students_list:
            st = i.get_name_class() + str(i.get_level())
            st_id = i._get_id()
            if cur_class == st and cur_id != st_id:
                print(i.get_iam_all())
                print("")



def main():
    current = -1
    iam = generate_students(count_students)
    dir = generate_director()
    
    while current != "q":
        print("[1] - root, [2] - director, [3] - student, [q] - quit")
        inp = input()
        print("")
        if inp == "q":
            print("пока")
            break

        try:
            current = int(inp)
        except:
            print("введите цифру 1,2,3 или букву q")
            continue
        
        if current in range(1, 4):
            current = int(inp)
            if current == root:
                print("введите пароль, назад [q]")
                passwd = input()
                if passwd == "root":
                    while current != "q":
                        print("работа со студентами [1],\n" \
                            "работа с директорами [2],\n" \
                            "прекратить работу школы [3],\n" \
                            "назад [q]\n")
                        i = input()
                        if i == "q":
                            break
                        try:
                            i = int(i)
                        except:
                            continue
                        
                        is_root(int(i))
                else:
                    print("неверный пароль")
            elif current == director:
                while current != "q":
                    print("я [1],\n" \
                        "все ученики [2],\n" \
                        "уволиться [3],\n" \
                        "остранить студента [4],\n" \
                        "провести контрольную работу по всем предметам [5],\n" \
                        "назад [q]\n")
                    i = input()
                    if i == "q":
                        break
                    try:
                        i = int(i)
                    except:
                        continue
                    new_dir = director_list_one[0]
                    is_director(int(i), new_dir, iam)
            else:
                while current != "q":
                    print("я [1],\n" \
                        "кто в моей группе [2],\n" \
                        "написать заявление [3],\n" + \
                        "назад [q]\n")
                    i = input()
                    if i == "q":
                        break
                    try:
                        i = int(i)
                    except:
                        continue
                    is_student(int(i), iam)
        else:
            print("введите цифру 1,2,3 или букву q")
        


if __name__ == '__main__':
    main()