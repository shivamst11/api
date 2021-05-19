import sqlite3
from flask_restful import Resource,reqparse
from models.user import  UserModel








class UserRegister(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="this field cannot be empty"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="this field cannot be empty"
                        )

    def post(self):
        data=UserRegister.parser.parse_args()
        connection=sqlite3.connect("data.db")
        cursor=connection.cursor()

        check=UserModel.find_by_username(data["username"])
        if check is None:
            insert_query="INSERT INTO users VALUES (NULL,?,?)"
            cursor.execute(insert_query,(data['username'],data['password']))
            connection.commit()
            connection.close()
            return {"msg":'item is created'},201
        else:
            return {'msg':'username is already exists'},400

    def get(self):

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        print_query="SELECT * FROM users"
        row=cursor.execute(print_query)
        data=row.fetchall()
        print(data)
        return {"data":data}




        

