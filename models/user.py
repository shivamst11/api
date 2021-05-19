import sqlite3

class UserModel:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        show_query = "SELECT * FROM users WHERE username=?"

        # using , in (username,,,) to make a tupple
        result = cursor.execute(show_query, (username,))
        # result is object  thats why using fectchone()

        # convert object to tuupple using fectchone
        row = result.fetchone()

        if row:

            user = cls(*row)  # this is class method and using args to pass the multiple variable
            # user=User(row[0],row[1],row[2])

        else:
            user = None
        connection.close()
        return user

    @classmethod
    def find_by_userid(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        show_query = "SELECT * FROM users WHERE id=?"

        result = cursor.execute(show_query, (_id,))

        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user