#	Найти сумму чисел списка стоящих на нечетной позиции
# # Пример:[1,2,3,4] -> 4

# numbers = [1, 2, 3, 4, 5, 6, 7]
# sum = 0
# for i in range(0,len(numbers),2):
#     sum = sum + numbers[i]
# print("Сумма чисел на нечетных позициях равна ", sum)


# # 2.	Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# # Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

# numbers = [1, 2, 3, 4, 5]
# powers = []
# i = 0

# for j in range (len(numbers)-1,(len(numbers)//2)-1,-1):
#     powers.append(numbers[i]*numbers[j])
#     i+=1    
# print(powers)


# # В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# # Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# numbers = [1.1, 1.2, 3.1, 5, 10.01]
# fract_numbers = numbers.copy()
# for i in range(len(fract_numbers)):
#     fract_numbers[i] = (fract_numbers[i]%1)
# print(fract_numbers)
# print ('%.2f' % (max(fract_numbers)-min(fract_numbers)))


# Написать программу преобразования десятичного числа в двоичное

# user_digit = int(input('Введите число '))
# dec_digit = user_digit
# to_bin_digit = ''
 
# while dec_digit > 0:
#     to_bin_digit = str(dec_digit % 2) + to_bin_digit
#     dec_digit = dec_digit // 2
 
# print(f'Число {user_digit} в двоичной системе равно', to_bin_digit)


# Написать программу преобразования двоичного числа в десятичное


# def bin_dec(digit):
#     number = 0
#     for i in range(0, len(digit)):
#         number += int(digit[i]) * (2**(len(digit) - i -1))
#     return number

# digit = input("Введите число в двоичной системе ")
# result = bin_dec(digit)
# print(f'Число {digit} в двоичной системе => число {result} в десятичной')


# # игра Быки и коровы


# import random
# from random import randint
# print()
# print('Вас превествует игра "Быки и Коровы". Попробуйте угадать 4х - значное число ')
# print('Когда Вы угадываете цифру из числа - вы получаете 1 Быка. Когда Вы угадываете цифру и ее положение -> 1 корову ')
# print()
# cow = 0
# bul = 0
# count = 0
# answer = str(randint(1000, 10000))
# user_answer = input('Введите 4х значное число ')

# while not user_answer.isdigit():
#     user_answer = input('Введите 4х значное число ')

# while True:
#     if(user_answer == answer):
#         print(f'Поздравляем, Вы угадали число c {count} попыток')
#         break
#     else:
#         count += 1
#     for i in range(len(answer)):
#         if(user_answer[i] == answer[i]):
#             cow += 1
#         elif(user_answer[i] in answer[:1]):
#             bul += 1
#     print(f'У вас {cow} коров и {bul} быков')
#     cow = 0
#     bul = 0
#     user_answer = input('Введите 4х значное число ')
   


