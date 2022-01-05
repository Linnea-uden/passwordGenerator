import random 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetAndNumbers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

def randomize_function():
    i = 0
    moreSecure = input("do you want to make the password more secure by using numbers and letters(yes or no): ")
    password = ""

    if moreSecure == "yes" or moreSecure == "Yes":
        while(int(i) < int(passwordLenght)):
            i += 1
            password = password + random.choice(alphabetAndNumbers)
    else:
        while(i < passwordLenght):
            i += 1
            password = password + random.choice(alphabet)
    print("Your password is: " + password)

print("Welcome to this password generator")
passwordLenght = input("Enter password lenght: ")
checkIsnumric = passwordLenght.isnumeric()
if checkIsnumric == True:
    randomize_function()
else:
    print("You have to enter a number")
    passwordLenght = input("Enter password lenght: ")
    randomize_function()




