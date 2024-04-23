# # Q1:
# user_first_name = input("Enter Your First Name: ")
# user_last_name = input("Enter Your Last Name: ")
# user_full_name = [user_first_name,user_last_name]
# reversed = user_full_name[::-1]
# print(f'{reversed[0]} {reversed[1]}')
# #------------------------------------------------------------
# # Q2:
# n = int(input("Enter number: "))
# print(n + int(f"{n}{n}") + int(f"{n}{n}{n}"))
# #------------------------------------------------------------
# # Q3:
# doc = 'Sample string:\na string you "don\'t" have to scape\nThis\nis a ....... multi-line\nheredoc string -------> example '
# print(doc)
# #------------------------------------------------------------
# # Q4:
# Bi = 3.14
# r = 6
# volume = 4/3 * Bi * pow(r,3)
# print(volume)
# #------------------------------------------------------------
# # Q5:
# base = float(input("Enter Triangle Base: "))
# height = float(input("Enter Triangle Height: "))
# area = 1/2 * base * height
# print(area)
# #------------------------------------------------------------
# # Q6:
# levels = 5
# for i in range(1, levels * 2):
#     if i <= levels:
#         stars = i
#     else:
#         stars = levels * 2 - i
#     for j in range(stars):
#         print("* ", end="")
#     print()
# #------------------------------------------------------------
# # Q7:
# word = input("Enter The Word: ")
# letters = list(word)[::-1]
# print(letters)
# #------------------------------------------------------------
# # Q8:
# for i in range(0,5,1):
#     if i == 3:
#         continue
#     print(i)
# #------------------------------------------------------------
# # Q9:
# a, b = 0, 1
# arr = []
# while a <= 100:
#     arr.append(a)
#     a, b = b, a + b
# print(arr)
# #------------------------------------------------------------
# # Q10:
# word = input("Enter Your Data: ")
# digit = 0
# alpha = 0
# for i in word:
#     if i.isalpha():
#         alpha += 1
#     elif i.isdigit():
#         digit += 1
# print(f'Number Of Digits Is: {digit}')
# print(f'Number Of Letters Is: {alpha}')
# #------------------------------------------------------------

my_list = [1, 2, 3, 4, 4, 5, 6, 1, 7]
arr = []

for num in my_list:
    if num not in arr:
        arr.append(num)

print(arr)




