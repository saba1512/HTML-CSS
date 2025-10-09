# გაქვს მსგავსი ტექსტი უნდა დათვალო a და the არტიკლი (The boy bought a book from the market. The book had a story about a king and a queen.)



information = "The boy bought a book from the market The book had a story about a king and a queen"

count_a = 0
count_the = 0

words = information.lower().split()

for i in words:
    if i == 'a':
        count_a += 1
    elif i == 'the':
        count_the += 1
print(count_a)
print(count_the)