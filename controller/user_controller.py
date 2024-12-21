from app import app
from model.user_model import Usermodel
from flask import request, send_file
from datetime import datetime
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
    

@app.route("/user/getall/limit/<limit>/page/<pageno>",methods=["GET"])
def user_pagination_controller(limit,pageno):
    return obj.user_pagination_model(limit,pageno)


@app.route("/user/<uid>/uploads/photo" , methods=["PUT"])
def user_fileupload_controller(uid):
    file=request.files["photo"]
    unique=str(datetime.now().timestamp())

    uniquename=unique.replace(".","")
    # print(uniquename)
    ext= (file.filename).split(".")
    extention=ext[len(ext)-1]
    filepath=f"uploads/{uniquename}.{extention}"
    file.save(filepath)
    return obj.user_fileupload_model(uid,filepath)

@app.route("/uploads/<filename>")
def display_photo(filename):
    return send_file(f"uploads/{filename}")