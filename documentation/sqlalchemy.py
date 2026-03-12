# alembic migrations
"""
What is Alembic?
    Alembic is a database migration tool for SQLAlchemy.
    It lets you track, version, and apply schema changes over time without manually altering the database.
    Example: adding a column, renaming a table, changing column types.
    """


"""
Connection polling 

A connection pool is a set of pre-created database connections that your application can reuse instead of creating
a new connection every time.

Why it matters:
Creating a new DB connection for every request is slow and resource-heavy.
A pool keeps a fixed number of connections ready.
Your app borrows a connection from the pool, uses it, then returns it.
Think of it like renting cars from a fleet instead of buying a new car every time.

 How SQLAlchemy Handles It

SQLAlchemy has built-in connection pooling. By default:

create_engine() uses a QueuePool.

Default parameters:


Key Parameters ::
    Parameter	    What it does
    pool_size	    Max number of persistent connections in the pool
    max_overflow	Extra connections allowed above pool_size
    pool_timeout	Seconds to wait for a free connection before raising error
    pool_recycle	Seconds after which a connection is reopened (prevents stale connections)
    pool_pre_ping	Checks if connection is alive before using it"""

from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:password@localhost:5432/product_db",
    echo=True,
    pool_size=5,         # max 5 connections in pool
    max_overflow=10,     # extra connections allowed beyond pool_size
    pool_timeout=30,     # wait up to 30 sec for a connection
    pool_recycle=1800    # recycle connection after 30 minutes
)

"""
Why It’s Important in Production
    Web apps like FastAPI can have many simultaneous requests.
    Without pooling, every request creates a new DB connection → slows down app → may hit DB connection limits.
    Pooling makes your app faster, scalable, and more reliable.
    """

