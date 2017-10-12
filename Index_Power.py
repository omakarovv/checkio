def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    if n > len(array) - 1:
        return -1
    else:
        return array[n] ** n

"""
Дан массив с положительными числами и число N. 
Вы должны найти N-ую степень элемента в массиве с индексом N. 
Если N за границами массива, тогда вернуть -1. 
Не забывайте, что первый элемент имеет индекс 0.
"""
