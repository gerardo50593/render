import csv 
import os 
import datetime
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv
load_dotenv()

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


archivo = open('user.csv')
reader = csv.reader(archivo)

i = 1
for row in reader:
    query = text("INSERT INTO users (username, password) VALUES (:username, :password)")
    db.execute(query, {"username": row[0], "password": row[1]})
    db.commit()