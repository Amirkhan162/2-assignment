a = int(input())
b = int(input())
c = int(input())
d = int(input())

if max(a, c) <= min(b, d):
    print("Overlapping")
else:
    print("Not Overlapping")