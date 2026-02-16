"""
python asyn programming is form of concurrent programming that allows the single programm therad to manage multiple or many i/o
bound task effecently by switching between them ... during the wating period 

it achive through the cooperative multitasking using the asyn or await syntax ,, primarly within the built in asynio libranry



Docstring for documentation.doc
"""
# async keyword is used before defining the function which specify that the the function as the asyncronous function which allows the task 
# to run without blocking the exectuion of other code ..  It is commonly used for handling tasks like network requests, 
# database operations or file I/O ..while waiting for the one task to execute will slow down the entire program

#?  Running Multiple Tasks Simultaneously
#?              -With the help of async, multiple tasks can run without waiting for one to finish before starting another.

import asyncio

async def task1():
    print("task 1 starte d ")
    await asyncio.sleep(3)
    print("task 1 complete ")

async def task2():
    print("task 2 started ")
    await asyncio.sleep(1)
    print("task 2 complete ")


async def main():

    await asyncio.gather(task1() , task2())

asyncio.run(main())


"""
task 1 started 
task 2 started
task 2 complete 
task 1 complete  """


# using async with http request :-
            # it is a very common method to use asyn with http like we have fetching the data from multiple urls 
            # in the synconous approch so it will block the execution of other request until it complete ...so however 
            # we have use the asyn with http request through which we can send the multiple request to fetch the data from url
            # s , which make the program must faster


