from app import app
from model.user_model import Usermodel
from flask import request
obj=Usermodel()
@app.route("/user/getall")
def user_getall_controller():   
    return obj.user_getall_model()
    # return "Thiss is user page" 

@app.route("/user/addOne", methods=["POST"])
def user_addone_controller():   
    return obj.user_addone_model(request.form)
    # return "Thiss is user page" 
