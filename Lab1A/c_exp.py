# Lab 1A - part C
# C = M^e mod p
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def cipher(message, e, p):
    if not is_prime(p):
        raise ValueError("p must be a prime number")
    return (message ** e) % p

print("C.1 8^13 mod 271 =", pow(8, 13, 271))
print("C.1 12^23 mod 973 =", pow(12, 23, 973))
print("C.2 8^5 mod 269 =", cipher(8, 5, 269))
for m, e, p in ((5, 5, 53), (4, 11, 79), (101, 7, 293)):
    print("C.3 message=%d e=%d p=%d -> %d" % (m, e, p, cipher(m, e, p)))
