def findPrimes(num):

    primes = []
    for i in range(0, num+1):
        if i > 1:
            for x in range(2,i):
                if (i % x) == 0:
                    break
            else:
                primes.append(i)

    return primes

if __name__ == "__main__":
    x = int(input("Enter a number:  "))
    print(findPrimes(x))
