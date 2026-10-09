a = int(input())
b = int(input())
c = int(input())

maximum = max(a,b)
minimum = min(a,b)
middle = (a + b + c) - maximum - minimum

print (f"maximum = {maximum}")
print (f"minimum = {minimum}")
print (f"middle = {middle}")