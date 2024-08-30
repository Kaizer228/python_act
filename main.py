userList = {}
userPasswordList = {}


def signUp():
    while True:
        print("-------Sign up-------")
        inputKey = input("Enter id: ")
        inputValue = input("Enter Username: ")
        inputPassword = input("Enter Password: ")

        if inputKey in userList:
            print("Key already exists.")
        else:
            userList[inputKey] = inputValue
            userPasswordList[inputKey] = inputPassword
            

        while True:
            option = input("Do you want to continue? y/n: ")

            if option.lower() == "y":
                break
            elif option.lower() == "n":
                print("List of users")
                for key in userList.keys():
                    print(f"Id {key} - Username - {userList[key]} - Password - {userPasswordList[key]}")
                return
            
def login():
    while True:
        print("-----Login-----")
        inputKey = input("Enter id: ")
        inputPassword = input("Enter Password: ")

        if inputKey in userList:
          if userPasswordList[inputKey] == inputPassword:
            print(f"User logged as {userList[inputKey]}")
            return
          else:
            print("Wrong password")
             
        else:
            print("User not found")

       



signUp()
login()
