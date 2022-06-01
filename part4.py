'''
______
PART 4
______
Write a program that prompts the user to enter two integer inputs. The program prints a string stating if the inputs are both positive, negative, if one of the inputs is zero, or if they have opposite signs. (Hint: this code can be written using only four code blocks, but you may find ways to do this using more.)

Four examples of what should appear on the console when this program runs (note: the test driver is case sensitive):

Enter a number:  3
Enter another number:  7
positive

Enter a number:  -5
Enter another number:  -2
negative

Enter a number:  7
Enter another number:  0
zero

Enter a number:  2
Enter another number:  -2
opposite
'''
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
#start writing your code below
#1) NUm 1 +
  #num2 +
  #num2 -
  #num2 == 0
#2) mum 1 -
#3) mun 1 == 0

if num1 > 0:
  if num2 > 0:
    print("Positive")
  elif num2 < 0:
    print("Opposite")
  elif num2 == 0:
    print("Zero")
elif num1 < 0:
  if num2 > 0:
    print("Opposite")
  elif num2 < 0:
    print("Negative")
  elif num2 == 0:
    print("Zero")
elif num1 == 0:
  print("Zero")
