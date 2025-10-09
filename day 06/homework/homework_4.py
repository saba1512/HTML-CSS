# ამ სიიდან list = [1,6,8,4,30,2,7,12,10,3,16,29,50,5] იპოვე ყველა  ლუწი და კენტი ციფრები  და ორივე ცალკცალკე სიაში მოათავსე და დაბეჭდე


list = [1,6,8,4,30,2,7,12,10,3,16,29,50,5]
even_numbers = []
odd_numbers = []

for i in list:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print(even_numbers)
print(odd_numbers)