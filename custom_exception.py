#Try to raise a custom exception.

def message(name):
    print("Hello",name)




name = str(input("Enter the name: "))

if name == "monkey":
    try:
        raise NameError("I hate you")

    except NameError:
        print('An exception flew by!')
        raise

else:
            message(name)