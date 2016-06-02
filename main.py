import csv
import datetime


def welcome():
    hello = input("\nWould you like to login? Y/n ").lower()
    if hello != "n":
        login()
    else:
        print("Goodbye")
        exit()


def check_field(name, field):
    with open("user_info.csv") as infile:
        user_data = csv.DictReader(infile, fieldnames=[
            "username", "password", "full_name", "fav_beer", "date_created"])
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
            user_data = csv.DictReader(infile, fieldnames=[
                "username", "password", "full_name", "fav_beer", "date_created"])
            for user in user_data:
                if login_user_name == user["username"]:
                    print(user)
        logout_or_create()
    else:
        print(" ! Not a valid entry !")
        welcome()


def logout_or_create():
    logout = input("\nLog[O]ut or [C]reate a new user? ").lower()
    if logout == "c":
        new_user()
    else:
        welcome()

welcome()
