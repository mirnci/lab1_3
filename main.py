n = int(input("Введите количество чисел и числа: "))
arr = []

for i in range(n):
    arr.append(int(input()))

order = input("Введите направление сортировки (asc/desc): ")

for i in range(n):
    for j in range(0, n - i - 1):
        if (order == "asc" and arr[j] > arr[j + 1]) or \
           (order == "desc" and arr[j] < arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Результат сортировки:", arr)