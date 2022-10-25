s = input("Enter a string: ")
n = int(input("Enter a no.: "))
a = s[::-1]
z = ""
for i in range(0, len(a), n):
    # print(a[i:n+i])
    z = z + " " + a[i:n+i]
print(z[::-1])
