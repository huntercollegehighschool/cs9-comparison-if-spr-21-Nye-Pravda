'''
______
PART 3
______
Write a program that asks the user to input one integer. The program will then print two strings, one stating if it's positive, negative, or zero, and another that states whether or not is is divisible by 3. (Hint: to check divisibility by 3, you will find using the modulus(%) operation very helpful.)

3 examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

Enter a number:  -2
negative
not divisible by 3

Enter a number:  0
zero
divisible by 3

Enter a number:  5
positive
not divisible by 3
'''
intg = int(input("Enter an integer: "))
#write your code below
if intg == 0:
  print("Zero")
  print("Divisible By 3")
if intg > 0:
  print("Positive")
  if (intg % 3 == int):
    print("Divisible By 3")
  else:
    print("Not Divisible By 3")
if intg < 0:
  print("Negative")
  if (intg % 3 == 0):
    print("Divisible By 3")
  else:
    print("Not Divisible By 3")