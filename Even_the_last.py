def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) == 0:
        return False

    b = 0
    for index in range(len(array)):
        if index % 2 == 0 and index <= 20:
            b = b + array[index]
    return b * array[index]

"""
Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд), затем перемножить эту сумму и последний элемент исходного массива. Не забудьте, что первый элемент массива имеет индекс 0.
Для пустого массива результат всегда 0 (ноль).
Входные данные: Список (list) целых чисел (int).
Выходные данные: Число как целочисленное (int).
"""
