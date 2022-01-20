# from email.policy import default
# from msilib import schema
# from tkinter.messagebox import NO
# from turtle import title
from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id : int = Field(default=None)
    title : str = Field(default=None)
    content : str = Field(default=None)
    class Config:
        schema_extra = {
            "post_demo" : {
                "title": "some title about animals",
                "content" : "some content about animals"
            }
        }

class UserSchema(BaseModel):
    fullname  : str = Field(default=None)
    email : EmailStr = Field(default= None)
    password : str = Field(default = None)
    class Config:
        the_schema = {
            "user_demo":{
                "name":"Help",
                "email":"help@gmail.com",
                "password":"1234"
            }  
        }        
class UserloginSchema(BaseModel):
    email : EmailStr = Field(default= None)
    password : str = Field(default = None)
    class Config:
        the_schema = {
            "user_demo":{
                "email":"help@gmail.com",
                "password":"1234"
            }
        }