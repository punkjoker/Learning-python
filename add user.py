def new_use():
    confirm= "N"
    while confirm != "Y":
        username = input("Enter the name of the user tto add: ")
        print("Use the name '"+ username + "'? (Y/N)")
        confirm = input().upper()
        os.system("sudo adduser " + username)