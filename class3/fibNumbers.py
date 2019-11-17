first = 2
second = 1
for i in range(1,23):
    fibonacci = first + second
    second = first
    first = fibonacci
print(fibonacci)
