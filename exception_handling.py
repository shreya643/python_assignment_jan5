#Write Python code to demonstrate the use case of exception handling. Try including else and finally syntax as well.

def divide(num):
    print(500/num)

user = int(input("Enter the number you want to divide 500 with:"))

try:
    divide(user)

except:
    print("Zero is not allowed.")
else:
    print("The division is successful")

finally:
    print("The program terminated.")
