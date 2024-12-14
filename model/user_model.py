import mysql.connector
import json

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
        print(result)
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No data found"
        
    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO user(username,email,mobile,password) VALUES('{data['username']}','{data['email']}','{data['mobile']}','{data['password']}')")
        return "Data added succesfully"