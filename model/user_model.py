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
            res=make_response({"Data":result},200)
            res.headers['Access-Control-Allow-Origin']="*"
            return res
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
        
    def user_patch_model(self,data,id):
            qry="UPDATE user SET "
            for key in data:
                qry+= f"{key}='{data[key]}',"

            qry = qry[:-1] + f" WHERE id={id}"
            # return qry
            self.cur.execute(qry)
            return make_response({"message":"Data updated succesfully"},200)
    
    def user_pagination_model(self,limit,pageno):
        limit=int(limit)
        pageno=int(pageno)
        start=(pageno*limit)-limit
        qry=f"SELECT * FROM user LIMIT {start}, {limit}"
        self.cur.execute(qry)
        result=self.cur.fetchall()
        if len(result)>0:
            res=make_response({"Data":result},200)
            return res
        else:
            return make_response({"message":"No data found "}, 204)