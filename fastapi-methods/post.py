from fastapi import FastAPI , Path , HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json
from model import Patient

def load():
    with open('data.json','r') as f:
        data=json.load(f)
    return data


def save(data):
    with open("data.json", "w") as f:
        json.dump(data,f)


app= FastAPI()

@app.post("/create")
def insert(patient:Patient):

    # check patient already exist or not
    data=load()
    if patient.id in data:
        raise HTTPException(status_code=404 , detail="patient already exist..")
    
    # add new patienet to database
    data[patient.id]= patient.model_dump(exclude=["id"])

    # save new data to data 
    save(data)

    return JSONResponse(status_code=201 , content={"message": "user created successfully"})


    

