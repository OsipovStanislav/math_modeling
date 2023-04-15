n = int(input())
if n % 400 % 4 % 100 != 0:
    print("Обычный")
else:
    print("Високосный")
