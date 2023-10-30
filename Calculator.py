import os
import sys
import subprocess
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


n1 = input("Enter a number: ")
while n1 == "":
    n1 = input("Enter a number: ")
op = input("Enter a operator (e.g. *, /, +, -): ")
while op == "":
    op = input("Enter a operator (e.g. *, /, +, -): ")
n2 = input("Enter another number: ")
while n2 == "":
    n2 = input("Enter a number: ")

if n1 == "pie":
    n1=3.14
if n2 == "pie":
    n2 = 3.14

num1 = float(n1)
num2 = float(n2)
result = 0

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "/":
    result = num1 / num2
elif op == "*":
    result = num1 * num2
else:
    print("you did not put the expected operator the Calculator will now be restarted")
    restart_program()

print("Result: " + str(result))

acceptance = input("Do you accept this answer Y/N: ")

if acceptance == "Y":
    restart = input("Do you want to restart the script? Y/N: ")
    if restart == "Y":
        restart_program()
elif acceptance == "N":
    print('Script will now exit')
else:
    print("you did not put the expected answer the Calculator will now be restarted")
    restart_program()