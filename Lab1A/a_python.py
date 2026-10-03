# Lab 1A - part A
import base64

# A.1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
for n in (91, 421, 1449):
    print("A.1", n, "prime?", is_prime(n))

# A.3
for s in ("Hello", "hello", "HELLO"):
    print("A.3", s, base64.b64encode(s.encode()).decode(), s.encode().hex().upper())

# A.4
print("A.4", base64.b64decode("bGxveWRz").decode())
print("A.4", bytes.fromhex("6E6170696572").decode())
bits = "01000001 01101110 01101011 01101100 01100101 00110001 00110010 00110011"
print("A.4", "".join(chr(int(b, 2)) for b in bits.split()))

# A.5
print("A.5", 53431 % 453)

# A.6
print("A.6", hex(0x43 | 0x21), hex(0x43 & 0x21), hex(0x43 ^ 0x21))

# A.7
val1 = 93
print("Dec:\t", val1)
print("Bin:\t", bin(val1))
print("Hex:\t", hex(val1))
print("Oct:\t", oct(val1))
print("Char:\t", chr(val1))

# A.9 and A.10
print("A.9 ", base64.b64encode(b"crypto").decode())
print("A.10", base64.b64encode(b"crypto1").decode())

# A.11
x = 41
print("A.11", x << 1, x << 2, x >> 1, x >> 2)

# A.12
def factors(n):
    f, d = [], 2
    while d * d <= n:
        while n % d == 0:
            f.append(d)
            n //= d
        d += 1
    if n > 1:
        f.append(n)
    return f
for n in (432, 600851475143, 999962000357):
    print("A.12", n, "=", " x ".join(map(str, factors(n))))
