#define variables
value = 0
new_pw = 0
orig_pw = 0
option = 0

#prints menu and allows user to enter an option
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    value = int(input(("Please enter an option: ")))
    return value

#to increase each value in the original password by 3
def encoder(orig_pw):
    new_encoded_pw = ""
    for num in orig_pw:
        num = int(num)
        new_pw = num + 3
        if new_pw >= 10:
            new_pw = new_pw % 10
        new_encoded_pw += str(new_pw)
    return new_encoded_pw

#what happens when each option is selected
if __name__ == '__main__':
    situation = True
    while situation:
        option = menu()
        if option == 1:
            orig_pw = str(input("Please enter your password to encode: "))
            encoded_pw = encoder(orig_pw)
            print("Your password has been encoded and stored!")
            print()
        elif option == 2:
            print(f"The encoded password is {encoded_pw} and the original password is {orig_pw}")
            print()
        elif option == 3:
            situation = False
        else:
            situation = False