import random
import time
import os
import array
import string
import colorama
from colorama import Fore, Style
import msvcrt

print(Fore.LIGHTCYAN_EX + "Welcome, to PyHash")
time.sleep(2)

Fore.LIGHTGREEN_EX

entry = input("Please enter the entry key: ")
if entry == "PyHashUser" or "PHU":
  pass
else:
  print(Fore.LIGHTRED_EX + "Failed key. Quitting.")
  exit()
  
print(Fore.GREEN + "Welcome, User.")
time.sleep(2)

Fore.LIGHTGREEN_EX

string = input("Enter your desired string: ")
if string == "":
  pass
else:
  pass

characterLib = "abcdef03689"

randomNum = 10, 20, 30, 5, 3, 6, 7, 26, 9, 32, 12, 8, 18, 33, 22, 42, 21, 32, 19

results = ''.join(random.choice(characterLib) for i in range(random.choice(randomNum)))
time.sleep(1)

print(results)

f = open("PyHash.txt", "w+", encoding = 'utf-8')

f.write(results)

print(Fore.CYAN + "Check your application directory for a file named 'PyHash.txt'")
time.sleep(2)
print(Fore.CYAN + "That's where your hashed string will be.")
time.sleep(1)
print("Press the 'ESC' key to close the program, or wait for the countdown to continue.")
aborted = False

for time_remaining in range(10, 0, -1):
  if msvcrt.kbhit() and msvcrt.getch() == b'\x1b':
    aborted = True
    break
    
    print(str(time_remaining))
    time.sleep(1)
    
if aborted:
  print("Program was closed")
  exit()
else:
  print("Program was not closed, continuing...")
  exit()
time.sleep(3)
