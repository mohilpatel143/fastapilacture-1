# from email.policy import default
# import imp
import fastapi
import uvicorn
from fastapi import FastAPI, Body, Depends
from app.model import PostSchema
from app.model import PostSchema, UserSchema, UserloginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer

posts = [
    {
        "id": 1,
        "title": "penguins",
        "text": "ijlewf kdnsjn dnbsbd sdndc"
    },
    {
        "id": 2,
        "title": "tiger",
        "text": "ijlewf kdnsjn dnbsbd sdndc"
    },
    {
        "id": 3,
        "title": "kolas",
        "text": "ijlewf kdnsjn dnbsbd sdndc"
    }
]

users = []

app = FastAPI()

# get - for tasting
@app.get("/", tags=["test"])
def greet():
    return {"Hello":"World!"}

# get posts
@app.get("/posts", tags=["posts"])
def get_posts():
    return{"data": posts}

# get single post {id}
@app.get("/posts/{id}", tags=["posts"]) 
def get_one_post(id : int):
    if id > len(posts):
        return {
            "error": "Post with this ID does not exist!"
        }   
    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }    

# post a blog post [a handler for creating a post]
@app.post("/posts", dependencies=[Depends(jwtBearer())], tags=["posts"])
def add_post(post : PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "info": "Post Added!"
    }            

@app.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)    
    return signJWT(user.email)

def check_user(data: UserloginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False    

@app.post("/user/login", tags=["user"])        
def user_login(user: UserloginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error": "invalid login details"
        }    
