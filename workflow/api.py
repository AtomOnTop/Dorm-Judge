#IMPORTING STANDARD LIBRARIES
import os
import sys
from fastapi import FastAPI
from pydantic import BaseModel, Field

#IMPORTING CUSTOM LIBRARIES 
#run pip install -e

from backend import class_models
from backend import encryption_gen_verify


#--------------#
app = FastAPI()
#--------------#

#---------HELPER FUNCTIONS---------#

#---------INITIALIZING SESSION STATE KEY-------#
SessionState = class_models.SessionStateKeys()

SessionState.logged_in = False
SessionState.user_id = ""
SessionState.role = ""
SessionState.current_view = ""
SessionState.selected_uid = ""

#---------LOGIN REQUESTS-------------#
class StudentLogin(BaseModel):
    roll_no : str = Field(examples=["Roll No."])
    password : str = Field(examples=["Password"])

@app.get("login/student/{roll_no}")
def Login_Verification(roll_no:str,password:str) -> tuple[str,str]:
    hashed_password = encryption_gen_verify.generate_password_hash(roll_no,password)
    login_payload = class_models.LoginCheckPayload()

    login_payload.user_id = roll_no
    login_payload.password = hashed_password
    login_payload.role = "student"

    if("""check_if_user_exists_function"""):
        user_exists_dictionary = {"user_id":roll_no,"password":password}
    else:
        user_exists_dictionary = {"user_id":None,"password":password}

    auth_payload = class_models.AuthPayload()
    auth_payload = encryption_gen_verify.process_login(login_payload,user_exists_dictionary)

    if(auth_payload.authenticated == True):
        return ("success",auth_payload.reason)
    else:
        if(auth_payload.reason == "invalid password"):
            return ("failure", auth_payload.reason)
        else:
            return ("failure", auth_payload.reason)





