from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer,Date


engine = create_engine('mysql+mysqldb://root:Wangmaonan1@localhost:3306/shiyanlou?charset=utf8')
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    type = Column(String(64))
    status = Column(String(64), index=True)
    school = Column(String(64))
    job = Column(String(64))
    level = Column(Integer, index=True)
    join_date = Column(Date)
    study_record = Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)