import os
# import requests
# import json
# import datetime
from flask import Flask ,render_template
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker


app =Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route('/')
def index():
    query = text("SELECT * from users")
    log = db.execute(query).fetchall()
    return render_template("index.html", lista=log)
