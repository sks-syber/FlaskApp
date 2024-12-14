from app import app
from model.user_model import Usermodel
obj=Usermodel()
@app.route("/user/getall")
def user_getall_controller():   
    return obj.user_getall_model()
    # return "Thiss is user page" 
