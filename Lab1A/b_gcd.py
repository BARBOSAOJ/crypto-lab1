# Lab 1A - part B (gcd)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

for a, b in ((4105, 10), (4539, 6)):
    print("B.1 gcd(%d, %d) = %d" % (a, b, gcd(a, b)))
for a, b in ((5435, 634), (5432, 634)):
    print("B.2 %d and %d co-prime? %s (gcd = %d)" % (a, b, gcd(a, b) == 1, gcd(a, b)))
