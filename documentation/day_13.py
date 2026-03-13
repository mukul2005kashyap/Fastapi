# async db access

"""
async db access means allowing the applications to access the db wihtout blocking the application while waiing for the 
response it allows the applications to handlle the multiple requests at the same time ...

Synchronous (Sync)
    In synchronous access, the program waits until the database query finishes before moving to the next task.

Example:
    esult = db.execute(query)
Problem:
    If the database takes time, the entire thread is blocked.
    The server cannot process other requests during that time.



Asynchronous (async)
    in asynchronous task the program does not block while the database is waiting it can process other request manwhile 

Example:
    result = await db.execute(query)

Benefits:
    Handles many concurrent users
    Better performance for APIs
    Non-blocking architecture


"""
# for doing asyncio db access in fastapi --you can do it by using the sqlalchemy asyncpg

"""
first u need to instal that 
    then you have to specift that in the databse url like
        "postgresql+asyncpg://user:password@localhost/dbname"

    and then you have to create the async engine by importing that

    then you have to import the async session and have to specify that while creating the session 
        AsyncSessionLocal = sessionmaker(
                                        engine,
                                        class_=AsyncSession,
                                        expire_on_commit=False
                                    )

"""

# query optimization ::

"""
Query optimization is a critical skill for database performance. It’s the process of making SQL queries run faster
and use fewer resources

Query optimization is the process of rewriting and tuning SQL queries so that the database engine can execute them
 more efficiently.

Goals:
    Reduce execution time
    Reduce CPU/memory usage
    Reduce I/O (disk reads/writes)

How Databases Execute Queries
    When you run a query:
        The DB engine parses your query.
        It generates possible execution plans.
        The optimizer chooses the plan with the lowest estimated cost.
        Key point: Even small changes in query structure can affect performance dramatically.


Common Query Optimization Techniques
Indexing
    Indexes are like a table of contents in a book.
    Without an index, the database does a full table scan (very slow).

Avoid SELECT *
    Only fetch required columns.

Use Joins Efficiently
    Prefer INNER JOIN over subqueries when possible.
    Ensure joined columns are indexed.

Filter Early
    Apply WHERE clauses as early as possible.
    Don’t fetch unnecessary rows.
"""

# N+1 problem 

"""
The N+1 problem is a common database performance issue, especially in ORMs like SQLAlchemy, Django ORM, or Hibernate.

What is the N+1 Problem?
    It happens when an application makes:
    1 query to fetch a list of records
    then N additional queries to fetch related data for each record
    So total queries become:
    1 + N queries

This kills performance when N is large.
     Example
        Suppose we have two tables:
        User
        -----
        id | name

        Orders
        ------
        id | user_id | product
            Code (Bad Example)
            users = session.query(User).all()

            for user in users:
                print(user.orders)
            Queries Generated
            SELECT * FROM users;              -- 1 query

SELECT * FROM orders WHERE user_id=1;         -- N queries
SELECT * FROM orders WHERE user_id=2;
SELECT * FROM orders WHERE user_id=3;
SELECT * FROM orders WHERE user_id=4;

If there are 100 users → 101 queries 
This is the N+1 problem.

Why It Is Bad
Problems:

    Too many DB calls

    Slow API response

    Higher database load

? SOLUTION 
        use joinload 
        use selectin 
    
"""

# PERFORMANCE TUNUING 
"""
performance  tunning is the process of identifing the system bottlenecks , optimizing code , database querise , memory usage ,
the system infrastracture to improve the scalability , performance , effeciancy of the applications ....

or you can say that the perfprmance tunning means optimizin the system like (api , applications , database)
so it can run more faster , takes ferewer resources , and handle the more load for better performance ...

Where Performance Tuning Happens
    Main areas:
            Layer	                Example

            Application	            inefficient loops
            Database	            slow queries
            API	high                response time
            Network	                too many requests
            Infrastructure          CPU / RAM limits

            

?common performance problems 
        slow database queries 
        n+1 query problem 
        multiple api calls 

? performance tunnning techniques ::
        avoid select *
        use indexing 
        efficent looping 
        use joins properly 
        avoid subqueries when possible
        async processing 
        connection polling 

Performance tuning involves identifying system bottlenecks and optimizing database queries, indexing, caching, 
and application logic to improve response time and scalability. Techniques include query optimization, indexing,
caching with Redis, connection pooling, and asynchronous processing.

"""