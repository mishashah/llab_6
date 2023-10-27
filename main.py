#Misha Shah
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

# Victoria Capparelli (created decode function)
def decode(encoded_pw):
    decoded_pw = ""
    for dig in encoded_pw:
        curr_dig = int(dig)
        curr_dig = curr_dig - 3
        if curr_dig < 0:
            curr_dig = 10 + curr_dig

        decoded_pw += str(curr_dig)

    return decoded_pw



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
            # Victoria Capparelli (replaced the second {} with the decoder function)
            print(f"The encoded password is {encoded_pw} and the original password is {decode(encoded_pw)}")
            print()
        elif option == 3:
            situation = False
        else:
            situation = False