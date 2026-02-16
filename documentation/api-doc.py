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