import os
from contextlib import contextmanager
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from functools import lru_cache
from toubib.config.config import DBSettings

BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sqlalchemy_url = f"sqlite:///{BASE_DIR}/db/toubib_rwuwam.db"

engine = create_engine(
    sqlalchemy_url, pool_pre_ping=True, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()
meta = MetaData()
patient = Table(
    'patient', meta,
    Column('id', Integer, primary_key=True),
    Column("first_name", String, nullable=False),
    Column("last_name", String, nullable=False),
    Column("email", String, nullable=False),
    Column("date_of_birth", String, nullable=False),
    Column("sex_at_birth", String, nullable=False),
)
meta.create_all(engine)

# doctors = Table(
#     'doctors', meta,
#     Column('id', Integer, primary_key=True),
#     Column("first_name", String, nullable=False),
#     Column("last_name", String, nullable=False),
#     Column("hiring_date", String, nullable=False),
#     Column("specialization", String, nullable=False),
# )
# meta.create_all(engine)

@contextmanager
def session_scope() -> Generator:
    db = None
    try:
        # create a session using sqlalchemy
        db = SessionLocal()
        yield db
    finally:
        db.close()


@lru_cache
def create_session() -> scoped_session:
    """

    :rtype: object
    """
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    print("database-cache=====>>>", db_session)
    return db_session


def get_session() -> Generator[scoped_session, None, None]:
    Session = create_session()
    try:
        yield Session
    finally:
        Session.remove()
