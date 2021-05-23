from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import DateTime

engine = create_engine(
    'postgresql+psycopg2://postgres:docker@0.0.0.0:5400/postgres')


Session = sessionmaker(bind=engine)
Base = declarative_base()


class Portfolios(Base):
    __tablename__ = 'Portfolios'
    id = Column(Integer, primary_key=True)
    Price = Column(Integer)
    Ticker = Column(String(200))
    Name = Column(String(200))
    Description = Column(String(200))
    Type = Column(String(200))
    Link_for_update = Column(String(200))
    Total_expence_ratio = Column(Integer)
    Creation_price = Column(Integer)
    Cancellation_price = Column(Integer)
    Shares_Outstanding = Column(Integer)
    Benchmark_Level = Column(Integer)
    Time_of_update = Column(DateTime)

