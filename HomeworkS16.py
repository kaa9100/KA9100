#HOMEWORK 
"This is my answer"
def prompt_and_print():
  number1 = int(input("Please Enter your first number:"))
  number2 = int(input("Please Enter another number: "))

  Addz = (number1 + number2)
  Subz = (number1 - number2)
  dividz = (number1 / number2)
  Modz = (number1 % number2)
  Floz = (number1 // number2)
  Multiz = (number1 * number2)

  print("Addition:",Addz,",""Subtraction:",Subz,",""Multiplication:",Multiz,"Division:",dividz,",""Mod:",Modz,",""Floor:",Floz,".")

prompt_and_print()
print(__doc__)