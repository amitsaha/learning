from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# demo one to many relationship, reverse side one to many
# http://docs.sqlalchemy.org/en/rel_0_9/orm/basic_relationships.html#many-to-one

engine = create_engine('sqlite:///onemany.db')
Base = declarative_base()

class Member(Base):
    __tablename__ = 'member'

    id = Column(Integer, primary_key=True)
    dob = Column(DateTime, default='2000-10-10 10:10:10')

    def __init__(self, id):
        self.id = id

# create tables
Base.metadata.create_all(engine)
# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Populate
member = Member(1)
session.add(member)
session.commit()
