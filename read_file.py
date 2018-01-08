#Read the contents from the text file that you've created in Question 5.

with open("E:\\python\\primes2.txt","r")as fp:
    data=fp.read()
    print(data)