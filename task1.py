# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input())
flag = True
while flag:
    if (number < 100 or number > 1000):
        print("Wrong input, try again:")
        number = int(input())
    else:
        flag = False

numb1 = number % 10
numb2 = number / 10 % 10
numb3 = number / 100

print(int(numb1 + numb2 + numb3))