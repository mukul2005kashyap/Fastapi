from pydantic import BaseModel ,EmailStr,AnyUrl,Field,field_validator,model_validator,computed_field
from typing import List, Dict,Annotated,Optional

class Address(BaseModel):
    city: str
    state: str
    pin:int

class Patient(BaseModel):
    id : int= Field(description="enter the id you want to update",examples=["1"])

    name :str=Field(description="idhar name dalne ka kya")

    age : int=Field(gt=0,lt=100)

    weight : Annotated[float,Field(gt=0,strict=True)]

    allergies:Annotated[Optional[List[str]],Field(max_length=4, default=None)]

    contact:Dict[str,str]

    Bp:bool

    address: Address

    link:Optional[AnyUrl]= None

    # @field_validator("name")
    # @classmethod
    
#     def name_validate(cls,value):
#         if value[0]=='1':
#             raise TypeError("value should be ster ")
#         return value

# # modelvalidator

    # @model_validator(mode="after")
    # def age_check(cls,model):
    #     if model.age>=60 and "emergency" not in model.contact:
    #         raise ValueError("you are above 60 give the e cont")
    #     return model

# compute field

    # @computed_field
    # @property
    # def protine(self) ->int:
    #     return int(self.weight*2 )




# """
# annotated:
# optional:
# anyurl:
# emailstr:

# @fieldvalidator in pydantic is used to apply the coustom validation , logic or the modification  on the specific field 
# it also ensures the integritty by checcking or transforming the data before storing them into the models 

# ? @modelvalidator
# @model_validator is a decorator used when you want to apply validation logic on:

#     multiple fields together
#     full object validation
#     cross-field validation (example: password == confirm_password)

# ?@compute field-
# compute field is feature in pydantic by which you can create the field whose value cannont be provided by the user but automatically 
# calculated from the other field in models and include in the response 

# ? Nested models
# --nested models means you using one model inside the another model as a field 
#         -better organization of related data
#         -readeability 
#         -reuseability
#         -validation --neated models are validated automatically u dont need to validate them automaticlly 


# # """
# class Patient(BaseModel):
#     id : str
#     name :str 
#     city :str 
#     age:int 
#     gender :str
#     height: float
#     weight: float


#     @computed_field
#     @property
#     def bmi(self) -> int:
#         bmi=(self.weight/self.height*2)
#         return bmi
    
#     @computed_field
#     @property
#     def verdict(self) -> int:
#         verdict=(self.weight+self.height*2)
#         return verdict

from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    age: int
    weight: float
    contact: str

    class Config:
        orm_mode = True