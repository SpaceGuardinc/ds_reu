from typing import Final

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from singleton import SingletonMeta


class Database(metaclass=SingletonMeta):
    BASE: Final = declarative_base()

    def __init__(self):
        self.__engine = create_engine(f'postgresql+pg8000://postgres:UMxjcFACw67Bf@127.0.0.1:5433/breadfabric')
        session = sessionmaker(bind=self.__engine)
        self.__session = session()

    @property
    def session(self):
        return self.__session

    @property
    def engine(self):
        return self.__engine
