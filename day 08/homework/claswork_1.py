user = input("enter sentance: ")

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for i in user.lower():
    if i in vowels:
        vowel_count += 1
    elif i.isalpha():
        consonant_count += 1

print(vowel_count)
print(consonant_count)
