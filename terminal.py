name = input("Type in your username. ")
print("Welcome " + name)

correct_password = "1234"
attempts = 0
locked_out = False

while attempts < 3:
    password = input("Type in your password please. ")

    if password == correct_password:  # correct password → login
        print("You are now logged in.")
        break
    else:  # wrong password → count attempt
        attempts += 1
        if attempts < 3:
            print("Wrong password, try again.")
        else:
            print("ALERT! Too many wrong tries")
            print("YOU ARE LOCKED OUT")
            locked_out = True
    

if not locked_out and password == correct_password:
    while True:
        prompt = input("> ")
        if prompt == "whoami":
            print (name)
        elif prompt == "scan":
            print ("Scanning network... 3 devices found")
        elif prompt == "hack":
            print ("Hacking network... Success")
        elif prompt == "help":
            print ("whoami: user info")
            print ("scan: scans network")
            print ("hack: attempts to hack the network")
            print ("exit: exits the program")
            print ("ls: lists files")
            print ("cd + directory: moves into specified directory")
            print ("cd: moves back to home directory")
            print ("cd .. : moves back by 1 directory")
        elif prompt == "ls":
            print ("/home/" + name)
            print ("documents/")
            print ("downloads/")
            print ("notes.txt")
        elif prompt == "cd documents/":
            print ("Empty")
        elif prompt == "cd downloads/":
            print ("Empty")
        elif prompt == "cat notes.txt":
            print ("I love apples")
        elif prompt == "cd":
            print ("/home/" + name)
        elif prompt == "cd ..":
            print ("/home/" + name)
        elif prompt == "exit":
            break 
        else:
            print ("Command unknown, type help for a command list")