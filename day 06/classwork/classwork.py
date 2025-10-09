# num = [89,4,5,56,8,34]

# print(sum(num))

# result = 0

# for i in num:
#     result += i
# print(result)

# result_len = 0

# for i in num:
#     result_len += 1
# print(result_len)


# print(len(num))

names = ['Nino', 'Giorgi', 'Lika', 'Ana', 'giga']

name = []

user = input("enter your name: ").lower()

for i in names:
    name.append(i.lower())

if user in name:
    print("yes")
else:
    print("no")
