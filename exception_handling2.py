#Write a program to catch at least 3 exceptions while manipulating the dictionary data structure.


def square(num):
    print("The square is", num**2)
def cube(num):
    print("The cube is:",num**3)


user=input("Enter your choice: ")

choice = {
    "1": square,
    "2":cube
}


try:
    choice[user]

except KeyError:
    print("Invalid Choice")


else:
    num = int(input("enter the number you want to square/cube:"))
    if user==1:
        square(num)
    else:
        cube(num)

finally:
    print("The program terminated.")

