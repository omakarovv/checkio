def checkio(*args):
    if 0 < len(args) <= 20:
        a = max(args)
        b = min(args)
        c = a - b
        return c
    else:
        return 0
"""
Давайте поработаем с числами.
Дан массив чисел (float или/и int). Вам нужно найти разницу между самым большим (максимум) и самым малым (минимум) элементом. Ваша функция должна уметь работать с неопределенным количеством аргументов. Если аргументов нет, то функция возвращает 0 (ноль).
Числа с плавающей точкой представлены в компьютерах как двоичная дробь. Результат проверяется с точностью до третьего знака, как ±0.001
Прочитайте о том как работать с переменым числом аргументов.
Вх. данные: Переменное число аргументов как числа (int, float).
Вых. данные: Разница между максимумом и минимумом как число (int, float).
"""
