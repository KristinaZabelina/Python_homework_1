# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input('Введите трехзначное число: '))
sum = 0
while number > 0:
    m = number % 10
    sum = sum + m
    number = number//10
print(sum)
