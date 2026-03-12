"""
the main differnce between the flask and fast api is that the flask works on the wsgi server that supports synchronous programming 
but the fast api works with the ASGI server that supports the asynchronous programming by default 

? . Explain async and await in FastAPI. Why is it important
        fast api uses the async and aeait while application performing i/o bound task like databse handling , getitng the request from the server

        in fast api if we use async def then the server can handle the multiple request without blocking the execution of another therad ..
                if request is waiting for the databse response the server will switch to handle the another response .....

"""

# difference between the path parameters and the query parameters ---
"""
        path parameters are the part of the url path that are mandatory and that are used to pass the dynamic values...

        query parametrs are the optional key value parameters that are passed after the ? at the end of the url this are tipically used for the 
        operations like pagging sorting alering filteraton etc...

"""
# What is the purpose of response_model in FastAPI?
"""
Answer:
response_model ensures the API response follows a defined schema.
It helps in:

    hiding sensitive fields like password
    maintaining consistent API responses
    automatic documentation generation
"""

# @compute field 
"""
compute field is feature in pydantic by which you can create the field whose value cannont be provided by the user but automatically 
calculated from the other field in models and include in the response """

# fastapi project setup 
"""
FastAPI Project Setup (Best Folder Structure)
📌 Step 1: Create Project Folder
mkdir fastapi_project
cd fastapi_project

Step 2: Create Virtual Environment
        python -m venv venv


Activate:

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

Step 3: Install Required Packages
        pip install fastapi uvicorn


For production:
        pip install python-dotenv pydantic sqlalchemy

Step 4: Recommended Project Structure
fastapi_project/
│── app/
│   │── main.py
│   │── __init__.py
│   │
│   ├── routers/
│   │   │── user.py
│   │   │── product.py
│   │   │── __init__.py
│   │
│   ├── models/
│   │   │── user_model.py
│   │   │── __init__.py
│   │
│   ├── schemas/
│   │   │── user_schema.py
│   │   │── __init__.py
│   │
│   ├── database/
│   │   │── db.py
│   │   │── __init__.py
│   │
│   ├── services/
│   │   │── user_service.py
│   │   │── __init__.py
│   │
│   ├── core/
│   │   │── config.py
│   │   │── __init__.py
│   │
│   ├── utils/
│   │   │── helper.py
│   │   │── __init__.py
│
│── requirements.txt
│── .env
│── README.md
"""

# ROUTING
"""
routing is machanism that matches the client request (based on the http method or url path) to the server side end point 
        (means the function or the method) that you write to handle the request """

# pydantic models
"""
pydantic models are inherit by the pydantic. basemodel """

# Dependency injections 
"""
Dependency injection is a designed pattern where required dependecy / reuseable logic like 
authentication , configuration where injected into the endpointineasted of writing that manually multiple time we use thzat through depends 

"""

from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

def verify_token(token: str = "abc123"):
    if token != "abc123":
        raise HTTPException(status_code=401, detail="Invalid Token")
    return token

@app.get("/profile")
def get_profile(token: str = Depends(verify_token)):
    return {"message": "Welcome!", "token": token}

