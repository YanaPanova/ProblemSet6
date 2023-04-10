from cs50 import get_int

while True:
    w = get_int("Height: ")
    if w < 9 and w > 0:
        break

for i in range(0, w, 1):
    for j in range(0, w, 1):
        if (i+j < w-1):
            print(" ", end="")
        else:
            print("#", end="")
    print()
