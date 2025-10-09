list = [8,5,14,34,9,3,67,87,78]

even_count = []
odd_count = []

for i in list:
    if i % 2 == 0:
        even_count.append(i)
    else:
        odd_count.append(i)
print(even_count)
print(odd_count)

