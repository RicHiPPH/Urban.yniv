first = int(input("Введите число №1: " ))
second = int(input("Введите число №2: " ))
third = int(input("Введите число №3: " ))
if first == second == third :                #Если все числа равны между собой, то вывести 3
    print(3 , "Числа равны")
else:
    print(0," ---Одно из чисел не верно ")
if first == second or first == third or second == third :
    print(2, " ---Как минимум два числа равны")
else:
    print("Нет двух равный чисел ")
