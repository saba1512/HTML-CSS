# user = int(input("enter number 1: "))

# user_1 = int(input("enter number 2: "))

# print(user + user_1)


# user = int(input("enter your age: "))

# if user >= 18:
#     print("ok")
# else:
#     print("no")


student = int(input("enter your score: "))

if student > 90 and student <= 100:
    print("dimond")
elif student >= 51 and student <= 90:
    print("finish")
elif student >= 0 and student <= 50:
    print("failed")
else:
    print("enter 0-100")