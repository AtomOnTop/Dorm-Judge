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

#---------LOGIN REQUESTS-------------#
class StudentLogin(BaseModel):
    roll_no : str = Field(examples=["Roll No."])
    password : str = Field(examples=["Password"])

@app.post("login/student/")
def Login_Verification(info: StudentLogin) -> dict:
    hashed_password = encryption_gen_verify.generate_password_hash(info.roll_no,info.password)
    login_payload = class_models.LoginCheckPayload()

    login_payload.user_id = info.roll_no
    login_payload.password = hashed_password
    login_payload.role = "student"

    if("""TODO: check_if_user_exists_function"""):
        user_exists_dictionary = {"user_id":info.roll_no,"password":info.password}
    else:
        user_exists_dictionary = {"user_id":None,"password":info.password} #Will return user id as none if user does not exist

    auth_payload = class_models.AuthPayload()
    auth_payload = encryption_gen_verify.process_login(login_payload,user_exists_dictionary)

    if(auth_payload.authenticated == True):
        return {"status":"success","reason":auth_payload.reason}
    else:
        return {"status":"failure", "reason":auth_payload.reason}

#-------------RAISE COMPLAINT--------------#
class Student_Raise_Request(BaseModel):
    roll_no : str = Field(examples=["Roll No."])
    title : str = Field(examples=["Enter complaint title"])
    body: str = Field(examples=["Enter complaint body"])

#@app.post("/raise_request/write")
#def Write_Request_Handler(body:Student_Raise_Request):
#WIP



