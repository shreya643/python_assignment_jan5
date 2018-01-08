#Complete Question 4 but, by using the context manager.

my_list = list(range(0,100))
with open("E:\\python\\primes2.txt","w") as fp:
    for num in my_list:
        for i in range(2, num - 1):
            if (num % i == 0):
                break
        else:
            fp.write("{}\t".format(str(num)))