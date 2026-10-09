x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1 quadrant")
elif x < 0 and y > 0:
    print("2 quadrant")
elif x < 0 and y < 0:
    print("3 quadrant")
elif x > 0 and y < 0:
    print("4 quadrant")