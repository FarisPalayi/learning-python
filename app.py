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

while True:
  user_command = input('> ').lower()
  if user_command == 'help':
    print("start - to start the car")
    print("stop - to stop the car")
    print("quit - to exit")
  elif user_command == 'start':
    print("Car started... ready to go!")
  elif user_command == 'stop':
    print("Car stopped")
  elif user_command == 'quit':
    break
  else:
    print("Sorry! I don't understand that")
