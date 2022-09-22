# Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже,
# то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем
# столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком

list_Tongue = ["C", "Java", "Python", "C++",
               "C#", "Visual Basic", "JavaScript"]

list_cout = [x for x in range(1, len(list_Tongue) + 1)]


def list_Cort(list_1: list, list_2: list) -> list:
    i = 0
    while i < len(list_2):
        list_2[i] = list_2[i].upper()
        i += 1
    list_result = list(zip(list_1, list_2))
    return list_result


def Filtru(list_3: list) -> list:
    l_couti = []
    l_tong = []
    for couti, tong in list_3:
        l_couti.append(couti)
        l_tong.append(tong)

    list_5 = []
    for i in l_tong:
        sum = 0
        if len(i) > 1:
            list_4 = list(i)
            for z in list_4:
                sum += ord(z)
        else:
            sum += ord(i)
        list_5.append(sum)
    
    list_result = []
    list_6 = []
    list_7 = []
    iter = 0
    while iter < len(list_5):
        prov = False
        if len(str(list_5[iter])) > 1:
            list_4 = str(list_5[iter])
            for z in list_4:
                if int(z) == l_couti[iter]:
                    prov = True
        else:
            if list_5[iter] == l_couti[iter]:
                prov = True
        
        if prov:
            list_6.append(l_tong[iter])
            list_7.append(list_5[iter])

        if iter == len(list_5) - 1:
            list_result = list(zip(list_7, list_6))

        iter += 1
        
    print(list_5)
    return list_result

list_result = list_Cort(list_cout, list_Tongue)

list_result2 = Filtru(list_result)

print(list_result2)
