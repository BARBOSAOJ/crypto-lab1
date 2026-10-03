# Lab 1B - numbers station

cipher = "66475 19274 92028 78494 24146 68542 17507 39398 32348 59378 70636".split()
key = "66153 77185 10800 54937 48159 83271 12892 07132 34987 53954 23074".split()

# add digit by digit without carry
plain = ""
for c, k in zip(cipher, key):
    for i in range(5):
        plain += str((int(c[i]) + int(k[i])) % 10)
print("Result:", plain)

# AT-ONE-SIR checkerboard
top = {"0": "A", "1": "T", "3": "O", "4": "N", "5": "E", "7": "S", "8": "I", "9": "R"}
row2 = "BCDFGHJKLM"
row6 = "PQUVWXYZ."

text = ""
i = 0
while i < len(plain):
    d = plain[i]
    if d == "2":
        text += row2[int(plain[i + 1])]
        i += 2
    elif d == "6":
        text += row6[int(plain[i + 1])]
        i += 2
    else:
        text += top[d]
        i += 1
print("Message:", text)
