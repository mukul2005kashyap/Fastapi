from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus


# passward = quote_plus("Kashyap@2005psql")
db_url= "postgresql://postgres:Kashyap%402005psql@localhost:5432/product_db"

engine=create_engine(db_url)

session = sessionmaker(autocommit= False , autoflush=False ,bind=engine)
