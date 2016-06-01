import csv
import datetime


def welcome():
    hello = input("\nWould you like to login? Y/n ").lower()
    if hello != "n":
        login()
    else:
        print("Goodbye")
        exit()


def login_or_create():
    intro = input("Would you like to [L]ogin or [C]reate a new account? ").lower()
    if intro == "l":
        login()
    else:
        new_user()


def new_user():
    username = input("Enter a new username: ")

    with open("user_info.csv") as infile:
        user_data = csv.DictReader(infile, fieldnames=["username", "password", "full_name", "fav_color", "date_created"])
        for user in user_data:
            if username.lower() == user["username"].lower():
                print("That is not a valid username, try again.")
                new_user()

    password = input("Enter the password: ")
    full_name = input("Enter the full name: ")
    fav_color = input("What is {}'s favorite color? ".format(full_name))
    date_created = datetime.datetime.now()
    formatted_date = date_created.strftime("%B %-d; %Y %-I:%M %p")  # make less friendly

    user_input = "{},{},{},{},{}\n".format(username, password, full_name, fav_color, formatted_date)

    # write to file
    with open("user_info.csv", "a") as outfile:
        outfile.write(user_input)

    print(" * New user created *")
    login_or_create()


def login():
    login_user_name = input("Username: ")
    login_password = input("Password: ")

    with open("user_info.csv") as infile:
        user_data = csv.DictReader(infile, fieldnames=["username", "password", "full_name", "fav_color", "date_created"])
        # for user in user_data:
        #     print(user["username"])
        for user in user_data:
            if login_user_name == user["username"]:
                if login_password == user["password"]:
                    print(user)
                    logout_or_create()
                else:
                    print("1 * Not a valid entry *")
                    welcome()
        else:
            print("2 * Not a valid entry *")
            welcome()


def logout_or_create():
    logout = input("\nLog[O]ut or [C]reate a new user? ").lower()
    if logout == "c":
        new_user()
    else:
        welcome()

# welcome()
# new_user()
login()
