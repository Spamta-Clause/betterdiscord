import sys

from datastore import Datastore

ds = Datastore("database.db")

def print_groups(groups):
    for group in groups:
        print(f"{group[0]} - {group[1]}")

while True:
    username = input("Username : ")
    password = input("Password : ")
    login_attempt = ds.login(username)
    if login_attempt == None:
        print("Unknown username.")
        while True:
            register = input("Would you like to register a new user? Y/N : ")
            if register == "Y":
                username = input("Username : ")
                password = input("Password : ")
                try:
                    ds.add_user(username, password)
                    login_attempt = ds.login(username)
                    break
                except:
                    print("Username already in use.")
            elif register == "N":
                break
            else:
                print("Invalid option.")
        break
    elif login_attempt[1] != password:
        print("Incorrect password.")
    else:
        break
        

class User:
    def __init__(self, details):
        self.username = details[0]
        self.password = details[1]
user = User(login_attempt)
group_selected = 0

while True:
    action = input("Action : ")
    if action == "add user":
        username = input("Username : ")
        password = input("Password : ")
        ds.add_user(username, password)
    if action == "add group":
        name = input("Name : ")
        group_id = ds.add_group(name)
        ds.add_user_to_group(user.username, group_id)
    if action == "invite":
        if group_selected != 0:
            ds.add_user_to_group(input("Select user : "), group_id=group_selected)
        else:
            print("Select a group to invite a user.")
        
    if action == "get groups":
        print_groups(ds.get_groups(user.username))
    if action == "get users":
        for x in ds.get_users():
            print(x[0])
    if action == "enter group":
        groups = ds.get_groups(user.username)
        print_groups(groups)
        while True:
            group_id = int(input("Select group id : "))
            if any(group_id in group for group in groups) :
                group_selected = group_id
                break
            else:
                print("Invalid group id.")
    if "send" in action.split(" ",1)[0]:
        message = action.split(" ",1)[1]
        ds.add_message(user.username, message, group_selected)

    if action == "exit":
        break