from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root(): 
    return {"massage": "Hello World!"} 

@app.get("/hello/{name}") 
def say_hello(name: str): 
    return {"message": f"Hello {name}!"} 

@app.get("/hello") 
def say_hello1(name: str): 
    return {"message": f"Hello {name}!"} 