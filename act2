class UserClass:
    userList = {}

    def __init__(self, Uname, Upass):
        self.Uname = Uname
        self.Upass = Upass
        
    def registerController(self):
        if self.Uname in UserClass.userList:
            print("User name already exists")
        else:
            UserClass.userList[self.Uname] = self.Upass
            print("Successfully registered")
        
    def loginController(self):
        if self.Uname in UserClass.userList:
            if UserClass.userList[self.Uname] == self.Upass:
                print(f"Welcome {self.Uname}")
            else:
                print("Wrong password")
        else:
            print("User not found")
            
    def displayUserController(self):
        print("------USER LIST------")
        for key, Upass in UserClass.userList.items():
            print(f"{key}: {Upass}")

def main():
    while True:
        choice = int(input(" Register  [1] \n Login     [2] \n User list [3] \n Exit      [4] \n Enter choice: "))
        if choice == 1:
            uname = input("Enter user name: ")
            upass = input("Enter password: ")
            user = UserClass(uname, upass)
            user.registerController()
        elif choice == 2:
            uname = input("Enter user name: ")
            upass = input("Enter password: ")
            user = UserClass(uname, upass)
            user.loginController()
        elif choice == 3:
            user.displayUserController()
        elif choice == 4:
            break
        else:
            print("Invalid option.")

       

main()
