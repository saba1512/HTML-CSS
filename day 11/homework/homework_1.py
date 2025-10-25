# მომხმარებელს უნდა შეაყვანინო პაროლი რომელიც უნდა შეიცავდეს ციფრს და მინიმუმ 6 ასოს


while True:
    user = input("enter password: ")
    if len(user) < 6:
        print("password must be at least 6 characters long")
    else:
        have_digit = False
        for i in user:
            if i.isdigit():
                have_digit = True
        if have_digit:
            print("password accepted")
            break
        else:
            print("password must contain at least one digit")