"""
def joke():
    who = input("Knock Knock:")
    print(who)

    little = input("Little old Lady:")
    print(little)

    print("I didn't know that you could yodel!")

def main():
    joke()
    joke()

main()

#Functions should start with: [Def *name of function*():] then you fill up the body. After filling up
#you should call out the funtion outside the body.. *name of function*()
"""

def add():
    number1 = 5
    number2 = 6
    Results = (number1 + number2)
    return Results

def main():
    Holder = add()
    Mixed = Holder * 5
    print(Mixed)

main()
