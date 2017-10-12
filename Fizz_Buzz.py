def checkio(number):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"

        
    #replace this for solution
    return str(number)

"""
"Fizz buzz" это игра со словами, с помощью которой мы будем учить наших роботов делению. Давайте обучим компьютер.
Вы должны написать функцию, которая принимает положительное целое число и возвращает:
"Fizz Buzz", если число делится на 3 и 5;
"Fizz", если число делится на 3;
"Buzz", если число делится на 5; 
Число, как строку для остальных случаев.
Входные данные: Число, как целочисленное (int).
Выходные данные: Ответ, как строка (str).
"""
