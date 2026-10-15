import sqlite3, datetime



class Datastore:
    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def login(self, username):
        self.cursor.execute(
            """
            SELECT username, password
            FROM members
            WHERE username LIKE :username
            """,
            {
                "username": username
            }
        )
        results = self.cursor.fetchone()
        return results

    def get_groups(self, username):
        self.cursor.execute(
            """
            SELECT groups.group_id, groups.group_name
            FROM member_groups
            JOIN groups ON member_groups.group_id = groups.group_id
            WHERE username LIKE :username
            """,
            {
                "username":username
            }
        )
        return self.cursor.fetchall()

    def get_users(self):
        self.cursor.execute(
            """
            SELECT username
            FROM members
            """
        )
        return self.cursor.fetchall()
    def get_messages(self,gid):
        self.cursor.execute(
            """
            SELECT author, text, time
            FROM messages
            WHERE group_id = :gid
            ORDER BY time ASC
            """,
            {
                "gid":gid
            }
        )
        return self.cursor.fetchall()

    def add_user(self, username, password):
        self.cursor.execute(
            """
            INSERT INTO members (username, password)
            VALUES (:username, :password)
            """,
            {
                "username":username,
                "password":password
            }
        )
        self.connection.commit()

    def add_group(self, name):
        self.cursor.execute(
            """
            INSERT INTO groups (group_name)
            VALUES (:name)
            """,
            {
                "name":name
            }
        )
        self.connection.commit()
        return self.cursor.lastrowid

    def add_user_to_group(self, username, group_id):
        self.cursor.execute(
            """
            INSERT INTO member_groups (username, group_id)
            VALUES (:username, :group_id)
            """,
            {
                'username':username,
                'group_id':group_id
            }
        )
        self.connection.commit()

    def add_message(self, user, message, group_id):
        self.cursor.execute(
            """
            INSERT INTO messages (group_id, author, text, time)
            VALUES (:group_id, :author, :message, :time)
            """,
            {
                "group_id" : group_id,
                "author" : user,
                "message" : message,
                "time" : datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            }
        )
        self.connection.commit()