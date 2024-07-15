### Программа для тестирования времени работы различных типов данных в Python

import time

# Количество операций для тестирования
amount_operations = 100000000

def test_list():
    print('В Python динамический массив реализован в виде списков. Список это изменяющийся тип данных.')
    print('Тестируем время работы со списком на сто миллионов элементов.')
    lst = []
    start_time = time.time()
    for i in range(amount_operations):
        lst.append(i)
    end_time = time.time()
    print(f"В список добавили {amount_operations} элементов за {round(end_time - start_time, 4)} секунд.")

    print()

    print('Тестируем время обращения к элементу списка')

    start_time = time.time()
    if 99999999 in lst:
        print('Элемент найден', end=' ')
    end_time = time.time()
    print(f"Поиск элемента занял всего {round(end_time - start_time, 4)} секунд")


    start_time = time.time()
    for i in range(amount_operations):
        lst.pop()
    end_time = time.time()
    print(f"Удаление из списка {amount_operations} элементов произошло за {round(end_time - start_time, 4)} секунд.")


def test_tuple():
    print('*************************')
    print('Поскольку кортеж это неизменяемый тип данных протестируем создание и поиск элемента.')
    print('Тестируем время работы с кортежем на сто миллионов элементов.')
    start_time = time.time()
    tpl = tuple(range(amount_operations))
    end_time = time.time()
    print(f"Создание кортежа с {amount_operations} элементами составило {end_time - start_time:.4f} секунд.")


    print()

    print('Тестируем время обращения к элементу кортежа.')

    start_time = time.time()
    if 99999999 in tpl:
        print('Элемент найден', end=' ')
    end_time = time.time()
    print(f"Поиск элемента занял всего {round(end_time - start_time, 4)} секунд.")



def test_set():
    print('*************************')
    print('Тестируем время работы с множеством на сто миллионов элементов.')

    st = set()
    start_time = time.time()
    for i in range(amount_operations):
        st.add(i)
    end_time = time.time()
    print(f"В множество добавили {amount_operations} элементов за {round(end_time - start_time, 4)} секунд.")

    print()

    print('Тестируем время поиска элемента множества.')

    start_time = time.time()
    a = 99999999
    if a in st:
        print(f"Элемент {a} есть в множестве.")
    end_time = time.time()
    print(f"Поиск элемента занял всего {round(end_time - start_time, 4)} секунд.")


    start_time = time.time()
    for i in range(amount_operations):
        st.remove(i)
    end_time = time.time()
    print(f"Удаление из множества {amount_operations} элементов произошло за {round(end_time - start_time, 4)} секунд.")

def test_dict():
    print('***************************************')

    dct = {}
    start_time = time.time()
    for i in range(amount_operations):
        dct[i] = i
    end_time = time.time()
    print(f"В словарь добавили {amount_operations} пар ключ-значение за {round(end_time - start_time, 4)} секунд.")

    print()
    print('Тестируем время поиска по ключу в словаре.')

    start_time = time.time()
    a = 99999999
    if a in dct:
        print(f"Ключ {a} есть в словаре и его значение {dct[a]}.")
    end_time = time.time()
    print(f"Поиск ключа занял всего {round(end_time - start_time, 4)} секунд.")



    start_time = time.time()
    for i in range(amount_operations):
        del dct[i]
    end_time = time.time()
    print(f"Из словаря удалили {amount_operations} пар ключ-значение за {round(end_time - start_time, 4)} секунд.")

test_list()
test_tuple()
test_set()
test_dict()