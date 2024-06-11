#Describe the problem
# def my_function():
#     for i in range (1, 21):
#         if i == 20:
#             print("You got it.")
#         # else:
#         #     print (i)
# my_function()

#reproduce the bug
# from random import randint
# dice_img = ["1","2","3","4","5","6"]
# dice_num = randint(0,5)
# print(dice_img[dice_num])

#Play computer
# year = int(input("What is your year of birth? "))
# if year > 1980 and year <= 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a GenZ.")

#Fix the error
# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}")

#Print is your friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages? "))
# word_per_page = int(input("Number of words per page? "))
# total_words = pages * word_per_page
# print(f"The total words of the book is {total_words}")

#Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#         print(b_list)

# mutate([1,2,3,4,5,12])