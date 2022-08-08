import random
print("Welcome to random password Generator!!")

user = input("Do you want random password with alphabets,numbers and characters? (yes/no): ")
if user == "yes":
    characters = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*"
    password_length = int(input("Enter your Password length? "))
    random_password = []
    for i in range(password_length):
        random_password.append(random.choice(characters))
    final_password = ''.join(map(str, random_password))
    print("Your Random Password is: ", final_password)

elif user == "no":
    user1 = input("Do you want random password with alphabets and numbers only? (yes/no): ")
    if user1 == "yes":
        characters = "qwertyuiopasdfghjklzxcvbnm1234567890"
        password_length = int(input("Enter your Password length? "))
        random_password = []
        for i in range(password_length):
            random_password.append(random.choice(characters))
        final_password = ''.join(map(str, random_password))
        print("Your Random Password is: ", final_password)
    elif user1 == "no":
        user = input("Then you want random password with alphabets only.(yes): ")
        if user == 'yes':
            characters = "qwertyuiopasdfghjklzxcvbnm"
            password_length = int(input("Enter your Password length? "))
            random_password = []
            for i in range(password_length):
                random_password.append(random.choice(characters))
            final_password = ''.join(map(str, random_password))
            print("Your Random Password is: ", final_password)
        else:
            print("Invalid Entry")
            print("Thank You for using Password Generator.")
