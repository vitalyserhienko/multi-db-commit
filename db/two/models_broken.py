from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BrokenAccount(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(30))
