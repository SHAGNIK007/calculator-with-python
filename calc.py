first = input("Enter your first number : ")
second = input("Enter your second number : ")
first = int(first)
second = int(second)
print("select your operator (+,-,*,/,%)")
operator = input("Enter operator symbol : ")

if operator == "+":
   print(first + second)
elif operator == "-":
   print(first - second)
elif operator == "*":
   print(first * second)
elif operator == "/":
   print(first / second)
elif operator == "%":
   print(first % second)
else:
   print("Invalid Operation")