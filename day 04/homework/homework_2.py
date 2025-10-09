# შექმენი ორი ცვლადი და შეაყვანინე რიცხვები
# თუ პირველი ციფრი მეტია მეორეზე დაპრინტე რომ "პირველი მეტია მეორეზე "
# თუ მეორე მეტია პირველზე დაპრინტე რომ "მეორე მეტია პირველზე"
# სხვა შემთხვევაში "უდრის"


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is greater than second")
elif a < b:
    print("Second number is greater than first")
else:
    print("They are equal")