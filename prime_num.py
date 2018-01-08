#Extract prime numbers from my_list = list(range(0,100)), and write it to a text file.

my_list = list(range(0,100))
#my_list=list(filter(lambda x:x%2!=0,my_list))

fp = open("E:\\python\\primes.txt","w")

for num in my_list:
    for i in range(2,num-1):
        if (num%i == 0):
            break
    else:
        fp.write("{}\t".format(str(num)))
fp.close()