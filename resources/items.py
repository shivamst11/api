import sqlite3

from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.items import CheckModel,ItemModel







class Item(Resource):
    parser = reqparse.RequestParser()


    parser.add_argument('name',
                        type=str,
                        required=False,
                        help=" this field cannot be left blank"
                        )
    @jwt_required()
    def get(self, name):
        item=CheckModel.item(name)
        print(item)

        if item:
            return {"item":item[0]},200 if item else 404
    @jwt_required()
    def post(self, name):
        data=Item.parser.parse_args()
        item = CheckModel.item(name)
        if item:
            return {"msg":"Item is already exists"},400
        else:
            connection = sqlite3.connect("data.db")
            cursor = connection.cursor()

            put_query = "INSERT INTO items VALUES(?)"
            cursor.execute(put_query, (data['name'],))
            connection.commit()
            connection.close()
            return {"name":data["name"]},201



    def delete(self, name):
        connection=sqlite3.connect("data.db")
        cursor=connection.cursor()

        delete_query="DELETE FROM items WHERE name=?"
        cursor.execute(delete_query,(name,))
        connection.commit()
        connection.close()


    def put(self, name):
        data = Item.parser.parse_args()
        item = CheckModel.item(name)

        if item is None:
            try:
                ItemModel.insert(data["name"])
            except:
                return {"message": "An error occurred inserting the item."}
        else:
            try:
                ItemModel.update(name,data['name'])
            except:
                raise
                return {"message": "An error occurred updating the item."}
        return {"item":name},202







class Itemlist(Resource):
    def get(self):
        pass

