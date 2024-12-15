from app import app
from model.user_model import Usermodel
from flask import request
obj=Usermodel()
@app.route("/user/getall")
def user_getall_controller():   
    return obj.user_getall_model()
     

@app.route("/user/addOne", methods=["POST"])
def user_addone_controller():   
    return obj.user_addone_model(request.form)
     

@app.route("/user/updateone", methods=["PUT"])
def user_updateone_controller():   
    return obj.user_updateone_model(request.form)
    

@app.route("/user/deleteone/<id>", methods=["DELETE"])
def user_deleteone_controller(id):   
    return obj.user_deleteone_model(id)
    

@app.route("/user/patch/<id>", methods=["PATCH"])
def user_patch_controller(id):   
    return obj.user_patch_model(request.form,id)
    