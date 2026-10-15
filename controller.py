from datastore import Datastore
ds = Datastore("database.db")

import datetime

from sqlite3 import IntegrityError

class ExistingUser(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
class UnknownUser(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)
class IncorrectPassword(Exception):
    def __init__(self, message):
        super().__init__(message)
class User:
    def __init__(self, details):
        self.username = details[0]
        self.password = details[1]

def register_member(username, password):
    try:
        ds.add_user(username, password)
        login_attempt = ds.login(username)
        user = User(login_attempt)
        return user
    except IntegrityError:
        raise ExistingUser("Username already in members table.")
def login(username, password):
    login_attempt = ds.login(username)
    if login_attempt == None:
        raise UnknownUser("Username not found in members table.")
    elif login_attempt[1] != password:
        raise IncorrectPassword("Password does not match that found in members table.")
    else:
        user = User(login_attempt)
        return user

def get_groups(username):
    groups = ds.get_groups(username)
    return groups

def get_messages(group_id):
    results = ds.get_messages(group_id)
    messages = []
    for message in results:
        time = datetime.datetime.strptime(str(message[2]),"%Y%m%d%H%M%S").strftime("%d-%m-%y %H:%M:%S")
        messages.append((message[0],message[1],time))
    return messages

def send_message(author, message, group_id):
    ds.add_message(author, message, group_id)

def add_group(user, group_name):
    gid = ds.add_group(group_name)
    ds.add_user_to_group(user, gid)
    return gid

def add_user_to_group(user, gid):
    ds.add_user_to_group(user, gid)