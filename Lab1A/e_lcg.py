# Lab 1A - part E
# x = (a*x + c) mod m
def lcg(a, seed, c, m, count):
    x, out = seed, []
    for _ in range(count):
        x = (a * x + c) % m
        out.append(x)
    return out

print("E.1", lcg(21, 35, 31, 100, 5))
print("E.2", lcg(22, 35, 31, 100, 4))
print("E.3", lcg(954365343, 436241, 55119927, 1000000, 4))
print("E.4", lcg(2175143, 3553, 10653, 1000000, 4))
