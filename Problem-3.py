# Problem-3.py
a = int(input("Enter a number: "))
limit = a if a % 2 == 1 else a - 1
for i in range(1, limit + 1, 2):
    print(i, end=", " if i + 2 <= limit else "\n")
