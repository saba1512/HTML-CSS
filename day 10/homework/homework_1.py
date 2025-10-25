password = "garibikaci123"

# user = input("enter your password: ")

# while len(user) != len(password) or user != password:
#     if user == "exit":
#         print("bye")
#         break
#     else:
#         print("incorrect")
#         user = input("enter your password: ")
# else:
#     print("correct")


while True:
    user = input("enter your password: ")
    if user == "exit":
        print("bye")
        break
    elif user == password:
        print("correct")
        break
    else:
        print("incorrect") 