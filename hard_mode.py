import csv
import datetime

names_fields = ["username", "password", "full_name", "fav_beer", "date_created"]

def welcome():
    hello = input("\nWould you like to login? Y/n ").lower()
    if hello != "n":
        login()
    else:
        print("Goodbye")
        exit()


def check_field(name, field):
    with open("user_info.csv") as infile:
        user_data = csv.DictReader(infile, names_fields)
        for user in user_data:
            if name == user[field]:
                return True
        else:
            return False


def new_user():
    username = input("Enter a new username: ")
    if check_field(username, "username") is True:
        print(" ! That is not a valid username, try again !")
        new_user()
    password = input("Enter the password: ")
    full_name = input("Enter the full name: ")
    fav_beer = input("What is {}'s favorite beer? ".format(full_name))
    date_created = datetime.datetime.now()
    formatted_date = date_created.strftime("%x %X")

    user_input = "{},{},{},{},{}\n".format(username, password, full_name, fav_beer, formatted_date)

    # write to file
    with open("user_info.csv", "a") as outfile:
        outfile.write(user_input)

    print(" * New user created *")
    logout_or_create()


def login():
    login_user_name = input("Username: ")
    login_password = input("Password: ")

    if check_field(login_user_name, "username") and check_field(login_password, "password") is True:
        with open("user_info.csv") as infile:
            user_data = csv.DictReader(infile, fieldnames=["username", "password", "full_name", "fav_beer", "date_created"])
            for user in user_data:
                if login_user_name == user["username"]:
                    print(user)
        logout_or_create()
    else:
        print("0 ! Not a valid entry !")
        welcome()


def edit_user(username):
    with open("user_info.csv") as infile:
        user_data = csv.DictReader(infile, fieldnames=["username", "password", "full_name", "fav_beer", "date_created"])
        for user in user_data:
            if username == user["username"]:
                print(user)
                if input("Would you like to edit your information? Y/n ").lower() != "n":
                    choice = input("1 pw 2 favbeer 3 fullname 4 create new user 5 log out")
                    if choice == "1":
                        new_pw = input("Enter your new password: ")
                        user["password"] = new_pw
                        # print(user)

                        with open("user_info.csv", 'a') as outfile:
                            writer = csv.DictWriter(outfile, fieldnames=["username", "password", "full_name", "fav_beer", "date_created"])
                            print(writer)
                            # writer.writerow(user)
                            # edit_user()
                            # for line, row in enumerate(writer):
                            #     data = user.get(line, row)
                            #     writer.writerow(data)


                    elif choice == "2":
                        new_beer = input("Enter your new favorite beer: ")
                        user["fav_beer"] = new_beer
                    elif choice == "3":
                        new_full_name = input("Enter your new full name: ")
                        user["full_name"] = new_full_name
                    elif choice == "4":
                        new_user()
                    elif choice == "5":
                        welcome()
                    else:
                        print("You choose poorly")
                        edit_user(username)
                else:
                    logout_or_create()


def logout_or_create():
    logout = input("\nLog[O]ut or [C]reate a new user? ").lower()
    if logout == "c":
        new_user()
    else:
        welcome()


# welcome()
# login()
edit_user("dhcrain")
