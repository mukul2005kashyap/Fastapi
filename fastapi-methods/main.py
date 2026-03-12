# """
# '''what is fast api : -    FastAPI is a modern and high-performance Python web framework used to build APIs quickly and efficiently.
#                          Designed with simplicity it allows developers to create RESTful APIs using Python's type hints which also 
#                          enable automatic validation and error handling.

# feature of fastapi: -
#                         1) Automatic Documentation: FastAPI auto-generates interactive API docs using OpenAPI standard
#                         2)Data Validation: FastAPI uses Pydantic models to validate and serialize/deserialize request data automatically.
#                         3)Asynchronous Support: Supports async and await allowing non-blocking code for better performance in I/O-heavy apps.


# installation of fast api : - 

# setup venv : python -m venv venv 
#              venv/Scripts/Activate 


# Python version should be great than >= 3.7

# 1)  pip install fastapi 

# pip  show fastapi 

# check :- Version: 0.116.1

# install uvicorn 
# 2) pip install unicorn 

# create a main.py file root!
# ? uvicorn is a Asgi web server that is used to run fast api --
#         ASGI means:it can run FastAPI and handle multiple requests fast.
#         FastAPI needs a server to run, and that server is usually uvicorn.


# ? Pydantic -- pydantic is a data validation tool that is used to valdite the data means it checks that the data comes the fast api is in 
#     the correct format or not

#     asyn await--its like a asyncronous task means while one api request is perform or take a time to get execute so during that task 
#     it will perform the other task or it would run other request

# """


from fastapi import FastAPI , Path , HTTPException
from pydantic import BaseModel
import json 
import database_model
from config import engine , session

app = FastAPI()

database_model.Base.metadata.create_all(bind=engine)


def load():
    with open('data.json','r') as f:
        data=json.load(f)
    return data


@app.get("/")
def add():
    return {"message": "welcome to the crestwin"} 


@app.get("/view")

def show():
    db=session()
    db.query()
    data = load()
    return data

# # """
# # path parameters --
# #             path parametrs are the parametrs that you pass with or inside the urls paths
# #             they are used to send dynamic data like name id age pid etc......


# #     """

@app.get("/employee/{id}")
def display(id:str = Path(..., description="here you enter the employee id ", example="P002")):           #--it is used to enhance the readibility
                                                                                                        # validation metadata and documentation  
                                                                                                         # at your api end point 
    data=load()
    if id in data:
        return data[id]
    
#       return "details not found"
    raise HTTPException(status_code=404, detail="Employee of this id is not found...")

# # #?    HTTP Exception -- is a special built in exception in fastapi that is used to return the custom http error while something got wrong
# #         #?  while inested of writting the json or crashing the server , you can gracefully raise the error


# """
# # ?  query parameter are the special optional key value parameter that are append at the end of the url used to pass the additional data
# #             eith http url that are typicaly used for operations like pagging sorting alteration filltering searchinng etc...

# # """


from model import Patient,Address
Address1=Address(city="indore",state="Mp",pin=4520)


# patient_info=[
#     Patient(id=1, name="mukul", age="34",weight=60.3,allergies=["dust","dhoop","smell"],contact={"mobile":"939899380"},Bp=False,address=Address1),
#     Patient(id=2,name="Rahul",age="28",weight=72.5,allergies=["pollen", "milk"],contact={"mobile": "9876543210"},Bp=True,address=Address1),
#     Patient(id=3, name="aman", age="40", weight=80.0, allergies=["dust"], contact={"mobile":"9123456789"}, Bp=False, address=Address1),
#     Patient(id=4, name="neha", age="25", weight=55.2, allergies=["smell","cold"], contact={"mobile":"9988776655"}, Bp=False, address=Address1),
#     Patient(id=5, name="priya", age="30", weight=62.8, allergies=["dhoop","pollen"], contact={"mobile":"9012345678"}, Bp=True, address=Address1),
#     Patient(id=6, name="suresh", age="50", weight=78.4, allergies=["dust","smoke"], contact={"mobile":"9090909090"}, Bp=True, address=Address1)
# ]


from database_model import Product

product_info = [
    Product(name="Mukul", age=34, weight=60.3, contact="939899380"),
    Product(name="Rahul", age=28, weight=72.5, contact="9876543210"),
    Product(name="Aman", age=40, weight=80.0, contact="9123456789"),
    Product(name="Neha", age=25, weight=55.2, contact="9988776655"),
    Product(name="Priya", age=30, weight=62.8, contact="9012345678"),
    Product(name="Suresh", age=50, weight=78.4, contact="9090909090")
]

def initdb():

    db=session()
    db.query(Product).delete()
    db.commit()

    db.add_all(product_info)

    db.commit()

initdb()




# @app.get("/sho")
# def show():
#     return patient_info 


# @app.post("/add")
# def insert(patient:Patient):
#     for i in patient_info:
#         if i.id == patient.id:
#             raise HTTPException(status_code=401,detail="already exixt")
#     patient_info.append(patient)
#     return patient_info
    

# @app.put("/add")
# def update(id: int, patient: Patient):
#     for index, p in enumerate(patient_info):
#         if p.id == id:
#             patient_info[index] = patient
#             return {"message": "patient updated successfully"}

#     raise HTTPException(status_code=404, detail="not exist")

# @app.delete("/delete")
# def delet(id:int):
#     for i in range(len(patient_info)):
#         if patient_info[i].id==id:
#             del patient_info[i]
#             return "deleted successfully"
                        
#     return HTTPException(status_code=404 ,detail="patient not found")


"""
Operation       HTTP Method	       Endpoint

Create	           POST	            /users
Read All	       GET	            /users
Read One	       GET	            /users/{id}
Update	           PUT	            /users/{id}
Delete	           DELETE	        /users/{id}"""