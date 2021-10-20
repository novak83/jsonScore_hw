import random
import json

with open("score_list.json", "r") as score_file:
     score_list = json.loads(score_file.read())
     print("Top scores:" + str(score_list[:3])) # prikaz le prvih treh rezultatov

import datetime

x = datetime.datetime.now()
print(x)


def name():
     d = {}
     qs = dict(Fname='first name', Lname='last name')
     for k,v in qs.items():
         d[k] = input('Please enter your {}: '.format(v))
     return d

name()

secret = random.randint(1, 30)
attempts = 0

while True:
     guess = int(input("Guess the secret number (between 1 and 30): "))
     attempts += 1

     if guess == secret:
         score_list.append(attempts)
         score_list.sort()

         with open("score_list.json", "w") as score_file:
             score_file.write(json.dumps(score_list))
         print("You've guessed it - congratulations! It's number " + str(secret))
         print("Attempts needed: " + str(attempts))
         break
     elif guess > secret:
         print("Your guess is not correct... try something smaller")
     elif guess < secret:
         print("Your guess is not correct... try something bigger")
