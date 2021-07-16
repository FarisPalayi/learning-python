# name = input("Type your name \n")
# print(f"So your name is {name}")

# name = "john smith"
# print(name.lower())
# print(name.find('h'))  # search
# print(name.replace('john', 'drake'))
# print('john' in name)  # check to see if it includes
# print(10 / 3)
# print(10 // 3)  # returns an integer
# print(2 ** 3)  # power
# print(round(-4.1))
# print(abs(-3))  # always returns a positive value

# import math  # modules

# print(math.ceil(4.4))

# is_high_income = True
# has_good_credit = True
# has_criminal_record = False

# if is_high_income and has_good_credit:
#   print("He is rich man")

# if is_high_income or has_good_credit:
#   print("He is kinda rich")

# if (is_high_income or has_good_credit) and not has_criminal_record:
#   print("yep, he is eligible I guess")

# i = 0
# while i <= 10:
#   print('*' * i)
#   i += 1
# print("done")

# GUESS GAME

# import random

# print('''
# Guess The Number 
# Hint: it's between 1-10(10 is excluded)
# ''')

# user_guessed = ''
# secret_number = random.randint(0,9)

# guess_count =  1
# guess_limit = 3

# while guess_count <= guess_limit:
#   user_guessed = int(input('Guess: '))
#   guess_count += 1
#   if user_guessed == secret_number:
#     print("You won!")
#     break
# else:
#   print('You lost!')


# Car Game

# user_command = ''
# started = False

# while True:
#   user_command = input('> ').lower()
#   if user_command == 'help':
#     print("start - to start the car")
#     print("stop - to stop the car")
#     print("quit - to exit")
#   elif user_command == 'start':
#     if started:
#       print('Car is already started')
#     else:
#       print("Car started... ready to go!")
#     started = True
#   elif user_command == 'stop':
#     if not started:
#       print("Car is already stopped")
#     else:
#       print("Car stopped")
#     started = False
#   elif user_command == 'quit':
#     break
#   else:
#     print("Sorry! I don't understand that")
# price = 0

# for i in [10, 20, 30]:
#   price += i

# print(price)

# for x in range(4):
#   for y in range(3):
#     print(f"({x}, {y})")

#  Print an F

# numbers = [5, 2, 5, 2, 2]

# for i in numbers:
#   f = ''
#   for j in range(i):
#     f += 'x'
#   print(f)

#  Largest number on the list

# numbers = [1,3,5,10,6,7]

# biggest_num = numbers[0]
# for number in numbers:
#   if number > biggest_num:
#     biggest_num = number
# print(biggest_num)

#  2d list / matrix

# matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]

# print(matrix[0][2])

# for row in matrix:
#   for item in row:
#     print(item)

#  List methods 

# list = [9, 5, 4, 2, 8, 2]
# list.append(23)
# list.insert(0, 10)  # to add it in desired index
# list.remove(2)  # removes the first occurrence of 2
# list.pop()  # removes the last item
# list.sort()
# list.reverse()
# list2 = list.copy()  # copies
# list.clear()  # to empty a list

# print(list)
# print(list2)

# string_list = ['what', 'a', 'when', 'oh', 'that']

# print(string_list.index('when'))  # to find the index of an item. if there's none, gets an error
# print('when' in string_list)  # returns a boolean value
# print(string_list.count('oh'))  # counts the occurrence of a specific items is in a list
# string_list.sort()
# print(string_list)

# #  Remove duplicates from a list

# numbers = [1,3,1]
# uniques = []

# for number in numbers:
#   if number not in uniques:
#     uniques.append(number)

# print(uniques)

# tuple = (1, 2, 3)  # it's like a list, but can't change any values

# coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# # onpacking
# x, y, z = coordinates  # does the same as the above code

# print(x)

# Dictionary

# customer = {
#   "name": "John Smith",
#   "age": 30,
#   "is_verfied": True
# }
# customer["job"] = "accountant"
# print(customer)

# print(customer["name"]) # returns error if doesn't exist
# print(customer.get("birthday", "jan 1"))  # 2nd argument - default value 

# number mapping

# phone = input('Enter phone number: ')

# digits_mapping = {
#   "0": "zero",
#   "1": "one",
#   "2": "two",
#   "3": "three",
#   "4": "four",
#   "5": "five",
#   "6": "six",
#   "7": "seven",
#   "8": "eight",
#   "9": "nine",
# }

# digits_in_characters = ''

# for digit in phone:
#   digits_in_characters += digits_mapping.get(digit, "!") + " "

# print(digits_in_characters)

# emoji mapping

# message = input(">")
# words = message.split(" ")

# emojis = {
#   ":)": "😀",
#   ":(": "😞"
# }

# output = ''

# for word in words:
#   output += emojis.get(word, word) + " "

# print(output)

# def greet_user(first_name, last_name):
#   print(f"Hi {first_name} {last_name}!")
#   print("Welcome aboard")


# greet_user('john', last_name='smith')  # positional arguments should always come first 
# print(greet_user('john', 'smith'))  # by default functions returns None


# def emoji_converter(message):
#   words = message.split(" ")
#   emojis = {
#     ":)": "😀",
#     ":(": "😞"
#   }
#   output = ''
#   for word in words:
#     output += emojis.get(word, word) + " "
#   return output


# print(emoji_converter(input(">")))

# Handling Errors

# try:
#   age = int(input("Age: "))
#   income = 20000
#   risk = income / age
#   print(age)
# except ZeroDivisionError:
#   print("Age cannot be zero")
# except ValueError:
#   print("Invalid value")

# Comments
#* never right comments that explains 'what the code does'
#* Use comments that explains whys and hows

# self is a reference to the current object
# so self.x means point1.x (point1 is an instance of Point class)
# class Point:
#   def __init__(self, x, y):  # constructor method
#     self.x = x
#     self.y = y

#   def move(self):
#     print("move")

#   def draw(self):
#     print("draw")

# point1 = Point(10, 20)
# point1.x = 20
# point1.draw()

# print(point1.x)


# class Person:
#   def __init__(self, name):
#     self.name = name

#   def talk(self):
#     print(f"Hi, I'm {self.name}")


# john = Person("John")
# john.talk()
# print(john.name)


class Mammal:
  def walk(self):
    print("walk")

class Dog(Mammal):  # Dog inherits Mammal
  def bark(self):
    print("bark")

class Cat(Mammal): 
  pass

dog1 = Dog()
dog1.walk()
dog1.bark()