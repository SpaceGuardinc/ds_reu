from typing import Final
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .singleton import SingletonMeta
from dotenv import load_dotenv

class Database(metaclass=SingletonMeta):
    load_dotenv()
    BASE: Final = declarative_base()
    def __init__(self):
        password = os.getenv("password")
        self.__engine = create_engine(f'postgresql+pg8000://postgres:{password}@127.0.0.1:5432/breadfabric')
        session = sessionmaker(bind=self.__engine)
        self.__session = session()

    @property
    def session(self):
        return self.__session

    @property
    def engine(self):
        return self.__engine
