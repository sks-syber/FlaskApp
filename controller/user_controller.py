from app import app
from model.user_model import Usermodel
obj=Usermodel()
@app.route("/user")
def user():
    return obj.userModel()
    # return "Thiss is user page" 
