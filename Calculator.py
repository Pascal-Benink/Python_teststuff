n1 = input("Enter a number: ")
op = input("Enter a opperator (e.g. *, /, +, -): ")
n2 = input("Enter another number: ")

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

print("Result: " + str(result))
