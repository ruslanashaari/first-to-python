from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

class Database:
        def __init__(self) -> None:
                self.server = os.getenv("DB_SERVER")
                self.db = os.getenv("DB_NAME")
                self.username = os.getenv("DB_USERNAME")
                self.secret = os.getenv("DB_SECRET")

        def connect(self):
                connnection_string = 'mysql+mysqlconnector://' + self.username + ':' + self.secret + '@' + self.server + '/' + self.db

                engine = create_engine(connnection_string)
                return engine.connect()