import math
def isprime(n: int) -> bool:
    if n <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                return False
        return True

n = int(input())
print(isprime(n))