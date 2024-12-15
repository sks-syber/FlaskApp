import mysql.connector
import json
from flask import make_response

class Usermodel():
    def __init__(self):
        try:   
            self.con=mysql.connector.connect(host="localhost",user="root",password="Sandeep",database="flask_data")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("Connection successful")
        except:
            print("Error in connecting database")

    def user_getall_model(self):
        self.cur.execute("SELECT * FROM user")
        result=self.cur.fetchall()
        # print(result)
        if len(result)>0:
            return make_response({"Data":result},200)
        else:
            return make_response({"message":"No data found"},204)
        
    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO user(username,email,mobile,password) VALUES('{data['username']}','{data['email']}','{data['mobile']}','{data['password']}')")
        return make_response({"message":"Data added succesfully"},200)
    
    def user_updateone_model(self,data):
        self.cur.execute(f"UPDATE user SET mobile='{data['mobile']}' WHERE id='{data['id']}'")
        return make_response({"message":"Data updated succesfully"},200)
    
    def user_deleteone_model(self,id):
        self.cur.execute(f"DELETE FROM user  WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({"message":"Data deleted succesfully"},200)
        else:
            return ({"message":"Nothing deleted"},202)
