import sqlite3

class ItemModel:
    def __init__(self,name):
        self.name =name;

    def json(self):
        return {'name':self.name}

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES(?)"
        cursor.execute(query, (item,))

        connection.commit()
        connection.close()

    @classmethod
    def update(cls, setname, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET name=? WHERE name=?"
        cursor.execute(query, (name, setname))

        connection.commit()
        connection.close()




class CheckModel:
    @classmethod
    def item(cls,name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        get_query = "SELECT * FROM items WHERE name=?"
        row = cursor.execute(get_query, (name,))
        item = row.fetchone()


        connection.close()

        return item
